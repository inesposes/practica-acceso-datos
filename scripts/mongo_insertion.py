import time
import requests
# from mongo_connection import connect_mongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['bicicorunha']
collection =db['stations']
# client, collection=connect_mongo()
print(collection)
print('Insertingg...')
while True: 
    print('entro')
    #API Request
    endpoint="http://api.citybik.es/v2/networks/bicicorunha"
    response=requests.get(endpoint)
    response_json=response.json()
    stations=response_json['network']['stations']
    print('sigo')

    try:
        # Insert in MongoDB
        print("try")
        result = collection.insert_many(stations)
        print('Inserted')
    except Exception as e:
        print("error")
    print("salgo")
    time.sleep(2) #Executed every 300sec (5min)
