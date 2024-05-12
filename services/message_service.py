# message_service.py

from pymongo import MongoClient
from models.models import Message

client = MongoClient("mongodb://localhost:27017/")
db = client["messenger"]
messages_collection = db["messages"]

def send_message(message: Message):
    message_dict = message.dict()
    messages_collection.insert_one(message_dict)
    return message
