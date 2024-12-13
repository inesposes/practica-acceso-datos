import time
import requests
from pymongo import MongoClient

client = MongoClient('mongodb://10.133.27.157:27017/')
db = client['newsdb']
collection =db['news']
#API Request
api_key = "5d286ef61a0b48a2b3c9ff72838cbec9"
headers = {
    'Authorization': f'Bearer {api_key}'
}
endpoint="http://newsapi.org/v2/everything?q=tech&apiKey=5d286ef61a0b48a2b3c9ff72838cbec9"
response=requests.get(endpoint, headers=headers)
response_json=response.json()
news=response_json['articles']
try:
    # Insert in MongoDB
    result = collection.insert_many(news)
except Exception as e:
    print("error"+ str(e))
