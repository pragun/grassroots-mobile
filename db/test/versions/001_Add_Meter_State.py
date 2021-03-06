from sqlalchemy import *
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from migrate import *

Base = declarative_base()

class MeterState(Base):
  __tablename__ = 'meter_states'
  id = Column(Integer, primary_key = True)
  created = Column(TIMESTAMP)
  balance = Column(Float)
  action = Column(String(255))

def upgrade(migrate_engine):
    Base.metadata.bind = migrate_engine
    MeterState.__table__.create(migrate_engine)

def downgrade(migrate_engine):
    Base.metadata.bind = migrate_engine
    MeterState.__table__.drop(migrate_engine)
