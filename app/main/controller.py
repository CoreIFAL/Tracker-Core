from app.models.user import User
from app.database import DB
import datetime

def list_active_sessions(list_users):
    active_sessions = []
    for i in list_users:
        #if i['event'][-1]['date'] == datetime.datetime.now().strftime("%d/%m/%Y") and i['event'][-1]['operation'] == 'logon' and 
        if len(i['event']) % 2 != 0:
            user = User(i['name'], i['event'][-1]['operation'], i['event'][-1]['computername'], i['event'][-1]['date'], i['event'][-1]['time'])
            active_sessions.append(user)
    return active_sessions
           
def get_data_by_username(username):
    user = DB.find_one("users", {'name':username})
    return user
