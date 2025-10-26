import os

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = os.getenv("MONGO_URI")
if not uri:
    raise ValueError("Please set the MONGO_URI environment variable")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

try:
    dbs = client.list_database_names()
    print("Connected successfully. Databases:", dbs)
except Exception as e:
    print("Connection failed:", e)
