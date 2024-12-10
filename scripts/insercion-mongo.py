import time
import requests
from pymongo import MongoClient

while True: 
    #API Request
    endpoint="http://api.citybik.es/v2/networks/bicicorunha"
    response=requests.get(endpoint)
    response_json=response.json()
    stations=response_json['network']['stations']

    # Insert in MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["bicicorunha"]
    collection = db["stations"]
    result = collection.insert_many(stations)
    time.sleep(300) #Executed every 300sec (5min)
