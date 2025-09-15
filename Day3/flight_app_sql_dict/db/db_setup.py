from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from .db_model import Base, Flight 

# db setup
engine = create_engine("sqlite:///flight_app_db.db", echo = True)
Base.metadata.create_all(engine) # creates tables
# session for sql operations 
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal() # for sql ops