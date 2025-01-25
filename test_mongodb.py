
from pymongo.mongo_client import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_DB_URI = os.getenv("MONGO_DB_URI")    


uri = MONGO_DB_URI

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)