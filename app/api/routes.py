from flask import Blueprint, request, jsonify
from app.schemas.client import ClientSchema
from app.core.db_postgres import db
from app.core.db_mongo import mongo_db
from sqlalchemy import text

api_blueprint = Blueprint("api",__name__)

@api_blueprint.route("/ping")
def ping():
  return {"message": "pong"}

@api_blueprint.route("/client", methods=["POST"])
def create_client():
  schema = ClientSchema()
  data = request.get_json()
  errors = schema.validate(data)
  if errors:
    return jsonify({"error": "Validation Error", "message": errors}), 400
  return jsonify({"message": "validate client", "data": data})

@api_blueprint.route("/db-check/postgres")
def check_postgres():
  try:
    db.session.execute(text("SELECT 1"))
    return jsonify({"status": "ok", "db": "PostgreSQL"}), 200
  except Exception as e:
    return jsonify({"status": "error", "message": str(e)}), 500

@api_blueprint.route("/db-check/mongo")
def check_mongo():
  try:
    collections = mongo_db.list_collection_names()
    return jsonify({"status":"ok", "db": "MongoDB", "collections": collections}), 200
  except Exception as e:
    return jsonify({"status": "error", "message": str(e)}), 500
