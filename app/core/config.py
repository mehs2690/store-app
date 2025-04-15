import os
from dotenv import load_dotenv

load_dotenv()

class Config:
  # PostgreSQL
  SQLALCHEMY_DATABASE_URI = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
    f"@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
  )
  SQLALCHEMY_TRACK_MODIFICATIONS = False

  # MongoDB
  MONGO_URI = f"mongodb://{os.getenv('MONGO_HOST')}:{os.getenv('MONGO_PORT')}"
  MONGO_DB = os.getenv("MONGO_DB")
