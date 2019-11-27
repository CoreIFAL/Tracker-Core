from app.models.user import User
from app.database import DB
import pymongo
import datetime

def list_active_sessions():
    active_sessions = []
    for i in DB.DATABASE['users'].find({'active':1}):
        print(i['name'], i['event'][-1]['date'], i['event'][-1]['computername'])
        if i['active'] == 1 and i['event'][-1]['date'] < datetime.datetime.now().strftime("%d/%m/%Y"):
            i['active'] = 0
            DB.DATABASE['users'].update_one({"name":i['name']}, {"$set":{"active":0}})
        active_sessions.append(i)
    return active_sessions

def how_many_users_active():
    query = {'active': 1}
    return DB.DATABASE['users'].count_documents(query)
           
def get_data_by_username(username):
    user = DB.find_one("users", {'name':username})
    return user

def how_many_access_by_labs():
    labs = ['L01.*', 'L02.*', 'L03.*', 'L04.*', 'L05.*', 'L06.*', 'PROJ.*', 'MINI.*']
    lista = []
    for i in labs:
        lista.append((i,list(DB.DATABASE['users'].aggregate([
                {'$project':{
                            'event':{
                                    '$filter':{
                                    'input':'$event',
                                    'as':'event',
                                    'cond':{'$eq':['$$event.operation','logon']}
                                    }
                                }
                            },
                },
                {'$unwind':'$event'},
                {'$match':{'$expr':{'$regexFind':{'input':'$event.computername', 'regex': i}}}},
                {'$group':
                    {
                        '_id':{'date':'$event.date'},
                        'total':{'$sum':1}
                    }
                }
            ]))))
    
    datas = {}
    index_lab = 0
    list_dates = DB.DATABASE['users'].distinct('event.date')
    list_dates.sort(key = lambda date: datetime.datetime.strptime(date, '%d/%m/%Y'))
    for i in list_dates:
        datas[i] = [0]*8 
    for i in lista:
        for j in range(len(i[1])):
            d = i[1][j]['_id']['date']
            t = i[1][j]['total']
            datas[d][index_lab] = t
        index_lab += 1
    
    return datas
