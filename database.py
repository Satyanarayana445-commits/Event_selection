from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine("postgresql://event_user:Event@localhost:5432/event",echo=True)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)
