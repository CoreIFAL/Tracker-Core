import pymongo
class DB(object):
         
    URI = "mongodb://localhost:27017"
          
    @staticmethod
    def init():
        client = pymongo.MongoClient(DB.URI)
        DB.DATABASE = client['tracker-dev']
        mydb = client['tracker-dev']
    @staticmethod
    def insert(collection, data):
        DB.DATABASE[collection].insert(data)
         
    @staticmethod
    def find_one(collection, query):
        return DB.DATABASE[collection].find_one(query)
    
    @staticmethod
    def find_all(collection):
        return DB.DATABASE[collection].find()
    
    @staticmethod
    def update_one(collection, query, data):
        return DB.DATABASE[collection].update_one(query, data)