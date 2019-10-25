from app.models.user import User
from app.database import DB
import pymongo
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

def how_many_access_by_labs():
    labs = ['L01.*', 'L02.*', 'L03.*', 'L04.*', 'L05.*', 'L06.*', 'PROJ.*', 'MINI.*']
    lista = []
    for i in labs:
        lista.append((i,mydb['users'].aggregate([
                {'$project':{
                            'event':{
                                    '$filter':{
                                    'input':'$event',
                                    'as':'event',
                                    'cond':{'$and':[
                                            {'$eq':['$$event.operation','logon']}
                                    ]}
                                }
                            },
                }},
                {'$unwind':'$event'},
                {'$match':{'$expr':{'$regexFind':{'input':'$event.computername', 'regex': i}}}},
                {'$group':
                    {
                        '_id':{'date':'$event.date'},
                        'total':{'$sum':1}
                    }
                }
            ])))
    return lista
