# user_service.py

from pymongo import MongoClient
from models.models import User

client = MongoClient("mongodb://localhost:27017/")
db = client["messenger"]
users_collection = db["users"]

def create_user(user: User):
    user_dict = user.dict()
    users_collection.insert_one(user_dict)
    return user
