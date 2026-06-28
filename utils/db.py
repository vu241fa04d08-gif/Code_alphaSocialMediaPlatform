from pymongo import MongoClient
import os

MONGO_URI = os.environ.get("MONGO_URI")

if not MONGO_URI:
    raise Exception("MONGO_URI is missing in environment variables")

client = MongoClient(MONGO_URI)

db = client["creators_hub"]

users_collection = db["users"]
profiles_collection = db["profiles"]
posts_collection = db["posts"]
requests_collection = db["requests"]
notifications_collection = db["notifications"]