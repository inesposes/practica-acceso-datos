import time
import requests
from pymongo import MongoClient
from datetime import datetime, timedelta

client = MongoClient('mongodb://10.133.27.157:27017/')
db = client['newsdb']
collection =db['news']
#API Request
api_key = "5d286ef61a0b48a2b3c9ff72838cbec9"
headers = {
    'Authorization': f'Bearer {api_key}'
}

while True: 
    date_now = datetime.now()
    date_yesterday = date_now - timedelta(days=1)
    endpoint='https://newsapi.org/v2/everything?q=tech&from='+date_yesterday.strftime('%Y-%m-%d')+'&to='+date_now.strftime  ('%Y-%m-%d')+'&sortBy=popularity&apiKey=5d286ef61a0b48a2b3c9ff72838cbec9'

    response=requests.get(endpoint, headers=headers)
    response_json=response.json()
    news=response_json['articles']
    try:
        # Insert in MongoDB
        result = collection.insert_many(news)
    except Exception as e:
        print("error"+ str(e))
    time.sleep(86400) #Executed every 300sec (5min)

