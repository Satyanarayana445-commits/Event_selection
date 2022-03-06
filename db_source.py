from models import Admin,User,UserEvent,Events
from sqlalchemy import create_engine,and_
from sqlalchemy.orm import sessionmaker
from fastapi import HTTPException,status
import jwt
from config import db_config

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"

class DBsource():
    instances=[]

    def __init__(self):
        self.__class__.instances.append(self)
    
    connection_url = ("postgresql://"+
                    db_config["user_name"]
                    + ":"
                    + db_config["password"]
                    + "@"
                    + db_config["host"]
                    +":"
                    + db_config["port"]
                    + "/"
                    + db_config["db_name"]
                )
    engine=create_engine(connection_url,echo=False)
    session_start = sessionmaker(bind=engine)




    # Functions related to users table
    @staticmethod
    def create_user(*args):
        session = DBsource.session_start()
        data = User(user_name=args[0],email=args[1],password=args[2])
        session.add(data)
        session.commit()
        session.close()


    @staticmethod
    def retrieving_user(id=0):
        session = DBsource.session_start()
        if(id==0):
            data=session.query(User).all()
            session.close()
            return data
        else:
            data=session.query(User).filter(User.id==id).first()
            session.close()
            return data

    @staticmethod
    def update_user(*args):
        session = DBsource.session_start()
        session.query(User).filter(User.id==args[0]).update({User.user_name:args[1],User.email:args[2],User.password:args[3]})
        session.commit()
        session.close()

    @staticmethod
    def delete_user(user_id=0):
        session = DBsource.session_start()
        data = session.query(User).filter(User.id==user_id).first()
        session.delete(data)
        session.commit()
        session.close()


    # Functions related to user_event table
    @staticmethod
    def book_event(*args):
        session = DBsource.session_start()
        num = "Event123"
        data=session.query(Events).filter(Events.event_name==args[0]).first()
        if(data != None):
            if(data.booking_status=="open"):
                if(session.query(UserEvent).filter(UserEvent.user_id==args[1]).count()==0):
                    data = UserEvent(event_name=args[0],ticket_number=num,user_id=args[1])
                    session.add(data)
                    session.commit()
                    session.close()
                else:
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Already registered for this event",
                        headers={"WWW-Authenticate": "Bearer"},
                    )
            else:
                raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Seats are not available for this event",
                        headers={"WWW-Authenticate": "Bearer"},
                    )
        else:
            raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="NO event with that name",
                        headers={"WWW-Authenticate": "Bearer"},
                    )


    @staticmethod
    def registered_event(id=0):
        session = DBsource.session_start()
        if(id==0):
            data=session.query(UserEvent).all()
            session.close()
            return data
        else:
            data=session.query(UserEvent).filter(UserEvent.user_id==id).all()
            session.close()
            return data

    @staticmethod
    def retrieving_user_ticket(user_ticket):
        session = DBsource.session_start()
        data=session.query(UserEvent).filter(UserEvent.ticket_number==user_ticket).all()
        session.close()
        return data

    # @staticmethod
    # def book_event(*args):
    #     session = DBsource.session_start()
    #     num = "Event123"
    #     session.query(UserEvent).filter(UserEvent.id==args[0]).update({UserEvent.event_name:args[1],UserEvent.ticket_number:num,UserEvent.user_id:args[2]})
    #     session.commit()
    #     session.close()

    # @staticmethod
    # def delete_user_event(user_event_id=0):
    #     session = DBsource.session_start()
    #     data = session.query(UserEvent).filter(UserEvent.id==user_event_id).first()
    #     session.delete(data)
    #     session.commit()
    #     session.close()


    # Functions related to admin table
    @staticmethod
    def create_admin(*args):
        session = DBsource.session_start()
        data = Admin(admin_name=args[0],email=args[1],password=args[2])
        session.add(data)
        session.commit()
        session.close()


    @staticmethod
    def retrieving_admin(id=0):
        session = DBsource.session_start()
        if(id==0):
            data=session.query(Admin).all()
            session.close()
            return data
        else:
            data=session.query(Admin).filter(Admin.id==id).first()
            session.close()
            return data

    @staticmethod
    def update_admin(*args):
        session = DBsource.session_start()
        session.query(Admin).filter(Admin.id==args[0]).update({Admin.user_name:args[1],Admin.email:args[2],Admin.password:args[3]})
        session.commit()
        session.close()

    # @staticmethod
    # def delete_admin(admin_id=0):
    #     session = DBsource.session_start()
    #     data = session.query(Admin).filter(Admin.id==admin_id).first()
    #     session.delete(data)
    #     session.commit()
    #     session.close()


    # Functions related to event table
    @staticmethod
    def create_event(*args):
        session = DBsource.session_start()
        data = Events(event_name=args[0],seat_count=args[1],event_summary=args[2],booking_status=args[3])
        session.add(data)
        session.commit()
        session.close()


    @staticmethod
    def retrieving_event(id=0):
        session = DBsource.session_start()
        if(id==0):
            data=session.query(Events).all()
            session.close()
            return data
        else:
            data=session.query(Events).filter(Events.id==id).first()
            session.close()
            return data

    @staticmethod
    def update_event(*args):
        session = DBsource.session_start()
        session.query(Events).filter(Events.id==args[0]).update({Events.event_name:args[1],Events.seat_count:args[2],Events.event_summary:args[3],Events.booking_status:args[4]})
        session.commit()
        session.close()

    @staticmethod
    def event_summary(event_id=0):
        session = DBsource.session_start()
        data = session.query(Events).filter(Events.id==event_id).first()
        session.close()
        return data.event_summary

    @staticmethod
    def token_generator(*args):
        print("hiiiii")
        session = DBsource.session_start()
        data = session.query(Admin).filter(Admin.admin_name==args[0]).first()
        token_data={}
        if(data != None):
            if data.password==args[1]:
                token_data = {
                    "id":data.id,
                    "admin_name":data.admin_name,
                    "email":data.email,
                    "password":data.password
                }
            else:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalied password",
                    headers={"WWW-Authenticate": "Bearer"},
                )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        print("admin_name",token_data["admin_name"])
        token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
        # token = jwt.encode(token_data,config_credential['SECRET'])
        session.close()
        return token