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


