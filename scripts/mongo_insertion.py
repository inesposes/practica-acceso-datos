import time
import requests
from mongo_connection import connect_mongo

client, collection=connect_mongo()
while True: 
    #API Request
    endpoint="http://api.citybik.es/v2/networks/bicicorunha"
    response=requests.get(endpoint)
    response_json=response.json()
    stations=response_json['network']['stations']

    # Insert in MongoDB
    result = collection.insert_many(stations)
    time.sleep(300) #Executed every 300sec (5min)
