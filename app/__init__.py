from flask import Flask
from flask_cors import CORS
from app.api.routes import api_blueprint
from app.core.config import Config
from app.core.db_postgres import db
from app.core.log_config import setup_logging
from app.errors.handlers import register_error_handlers

def create_app():
  app = Flask(__name__)
  app.config.from_object(Config)

  setup_logging()
  CORS(app)
  db.init_app(app)
  app.register_blueprint(api_blueprint)

  register_error_handlers(app)

  return app

