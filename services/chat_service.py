# chat_service.py

from pymongo import MongoClient
from models.models import Chat

client = MongoClient("mongodb://localhost:27017/")
db = client["messenger"]
chats_collection = db["chats"]

def create_chat(chat: Chat):
    chat_dict = chat.dict()
    chats_collection.insert_one(chat_dict)
    return chat
