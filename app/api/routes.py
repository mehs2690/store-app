from flask import Blueprint, request, jsonify
from app.schemas.client import ClientSchema

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

