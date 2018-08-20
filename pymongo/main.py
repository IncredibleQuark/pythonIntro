import pymongo
import datetime
from pymongo import MongoClient

myClient = MongoClient()
db = myClient.myDb
users = db.users

user1 = {"username": "nick", "password": "secure", "favourite_book": "Black", "hobbies": ["python", "games"]}
user_id = users.insert_one(user1).inserted_id

print("Inserted user", user_id)
print("Users in db", users.find().count())
print("Users with secure password :) ", users.find({"password": "secure"}).count())


current_date = datetime.datetime.now()
print(current_date)
old_date = datetime.datetime(2000, 1, 7)
print(old_date)

uid = users.insert_one({"username": "john", "date": current_date})
print(users.find({"date": {"$gt": old_date}}) .count())  # $gt stands for 'greater than' or $gte
print(users.find({"date": {"$exists": True}}).count())
print(users.find({"username": {"$ne": "nick"}}).count())  # $ne = not equal


# Custom  index
db.users.create_index([("username", pymongo.ASCENDING)])