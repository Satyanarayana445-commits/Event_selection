from fastapi import FastAPI,Depends
from db_source import DBsource
from fast_models import UserEvents,Users,Events,Admin
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm

app=FastAPI()

oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.post('/token')
async def token_generate(form_data: OAuth2PasswordRequestForm = Depends()):
    print("hiiii",form_data.username)
    token = DBsource.token_generator(form_data.username,form_data.password)
    return {"access_token":token,"token_type":"bearer"}

@app.get('/users')
def get_users():
    users=DBsource.retrieving_user()
    return users

@app.get('/get_one_user/{user_id}')
def get_one_user(user_id:int):
    users=DBsource.retrieving_user(user_id)
    return users

@app.post('/create_user')
def create_user(user:Users):
    DBsource.create_user(user.user_name,user.email,user.password)

# @app.put('/update_user/{user_id}')
# def update_user(user_id:int,user:Users):
#     DBsource.update_user(user_id,user.user_name,user.email,user.password)






@app.get('/user_events')
def get_user_event():
    user_event=DBsource.registered_event()
    return user_event

@app.get('/registered_event/{user_id}')
def registered_event(user_id:int):
    user_events=DBsource.registered_event(user_id)
    return user_events

@app.get('/get_user_ticket/{user_ticket}')
def get_user_ticket(user_ticket:str):
    user_ticket=DBsource.retrieving_user_ticket(user_ticket)
    return user_ticket

@app.post('/book_event')
def book_event(user_event:UserEvents):
    DBsource.book_event(user_event.event_name,user_event.user_id)

# @app.put('/user_event/{user_event_id}')
# def update_user_event(user_event_id:int,user_event:UserEvents):
#     DBsource.update_user_event(user_event_id,user_event.event_name,user_event.user_id)





@app.get('/admin')
def get_admin():
    users=DBsource.retrieving_admin()
    return users

@app.get('/get_one_admin/{admin_id}')
def get_one_admin(admin_id:int):
    users=DBsource.retrieving_admin(admin_id)
    return users

@app.post('/create_admin')
def create_admin(admin:Admin):
    DBsource.create_admin(admin.admin_name,admin.email,admin.password)

# @app.put('/update_admin/{admin_id}')
# def update_admin(admin_id:int,admin:Admin):
#     DBsource.update_admin(admin_id,admin.admin_name,admin.email,admin.password)





@app.get('/event')
def get_event():
    events=DBsource.retrieving_event()
    return events

@app.get('/get_one_event/{event_id}')
def get_one_event(event_id:int):
    event=DBsource.retrieving_event(event_id)
    return event

@app.post('/create_event')
def create_event(event:Events,token: str = Depends(oauth_scheme)):
    DBsource.create_event(event.event_name,event.seat_count,event.event_summary,event.booking_status)

@app.put('/update_event/{event_id}')
def update_event(event_id:int,event:Events,token: str = Depends(oauth_scheme)):
    DBsource.update_event(event_id,event.event_name,event.seat_count,event.event_summary,event.booking_status)

@app.get('/event_summary/{event_id}')
def get_event_summary(event_id:int,token: str = Depends(oauth_scheme)):
    event_summary=DBsource.event_summary(event_id)
    return event_summary