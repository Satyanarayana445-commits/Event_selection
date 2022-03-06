from database import Base
from sqlalchemy import Column, DateTime, Time, Date, ForeignKey, String, Integer, Float
from sqlalchemy.sql.sqltypes import VARCHAR,ARRAY,TEXT

class Admin(Base):
    """
    Mapping class for the admin_info table
    """

    __tablename__ = "admin_info"

    id = Column(Integer, primary_key=True,autoincrement=True)

    admin_name = Column(VARCHAR,nullable = True)

    email = Column(VARCHAR,nullable=True)

    password = Column(VARCHAR,nullable=True)

class Events(Base):
    """
    Mapping class for the events_info table
    """

    __tablename__ = "event_info"

    id = Column(Integer, primary_key=True,autoincrement=True)

    event_name = Column(VARCHAR,nullable = True)

    seat_count = Column(Integer,nullable=True)

    event_summary = Column(VARCHAR,nullable = True)

    booking_status = Column(VARCHAR,nullable=True)


class User(Base):
    """
    Mapping class for the users_info table
    """

    __tablename__ = "user_info"

    id = Column(Integer, primary_key=True,autoincrement=True)

    user_name = Column(VARCHAR,nullable = True)

    email = Column(VARCHAR,nullable=True)

    password = Column(VARCHAR,nullable=True)


class UserEvent(Base):
    """
    Mapping class for the user_event_info table
    """

    __tablename__ = "user_event_info"

    id = Column(Integer, primary_key=True,autoincrement=True)

    event_name = Column(VARCHAR,nullable = True)

    ticket_number = Column(VARCHAR,nullable=True)

    user_id = Column(Integer,ForeignKey('user_info.id',ondelete='CASCADE'))
