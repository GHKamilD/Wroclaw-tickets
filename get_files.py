from sqlalchemy import create_engine, ForeignKey, Integer, String, Column
from sqlalchemy.orm import sessionmaker, declarative_base
import uuid
import pandas
import os

Base = declarative_base()

class tickets(Base):
    __tablename__ = "tickets"
    ticketID = Column("ticketID", String, primary_key=True)
    ticketType = Column("ticketType", String)
    ticketCount = Column("ticketCount", Integer)
    ticketValue = Column("ticketValue", Integer)
    def __init__(self, ticketType, ticketCount, ticketValue):
        self.ticketID = str(uuid.uuid4())
        self.ticketType = ticketType
        self.ticketValue = ticketValue
        self.ticketCount = ticketCount


if not os.path.exists('wroclaw.db'):
    engine = create_engine('sqlite:///wroclaw.db')
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    file = pandas.read_csv("sprzedaz-biletow-i-iii-2024-fixed.csv", delimiter=';')

    file = file[file[file.columns[0]].str.contains('RAZEM')]
    file.reset_index(drop=True, inplace=True)
    for index, row in file.iterrows():
        ticket = tickets(
            ticketType=row[file.columns[0]],
            ticketCount=int(row[file.columns[1]].replace(" ", "")),
            ticketValue=int(row[file.columns[2]].replace(" ", ""))
        )
        session.add(ticket)
    session.commit()
