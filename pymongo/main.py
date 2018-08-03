import pymongo
from pymongo import MongoClient

myClient = MongoClient()

db = myClient.myDb

users = db.users

user1 = {"username": "nick", "password": "secure", "favourite_book": "Black", "hobbies": ["python", "games"]}

user_id = users.insert_one(user1).inserted_id

print("Inserted user", user_id)
