import datetime

from app.database import DB

class User(object):

    def __init__(self, name, operation, computername, date, time):
        self.name = name
        self.created_at = datetime.datetime.utcnow()
        self.event = {'date':date, 'computername':computername,'time':time, 'operation':operation}

    def insert(self):
        if not DB.find_one("users", {"name": self.name}):
            DB.insert(collection='users', data=self.insert_json())
        else:
            DB.update_one("users", {"name":self.name}, self.update_json())
            
    def insert_json(self):
        return {
            'name': self.name,
            'created_at': self.created_at,
            'event':[{
                    'date': self.event['date'],
                    'time': self.event['time'],
                    'computername': self.event['computername'],
                    'operation':self.event['operation']
                    }  
            ]
    }
    def update_json(self):
       return {
            "$push":{
                    'event':{
                            'date': self.event['date'],
                            'time': self.event['time'],
                            'computername': self.event['computername'],
                            'operation':self.event['operation']
                            }                                       
                    }
            }    
