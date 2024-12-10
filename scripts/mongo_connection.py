from pymongo import MongoClient

def connect_mongo(db_name='bicicorunha', collection='stations', uri = 'mongodb://localhost:27017/'):
    client = MongoClient(uri)
    db = client[db_name]
    collection =db[collection]
    return client, collection

