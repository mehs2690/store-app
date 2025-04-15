from flask import current_app
from pymongo import MongoClient
from app.core.config import Config

mongo_client = MongoClient(Config.MONGO_URI)
mongo_db = mongo_client[Config.MONGO_DB]
