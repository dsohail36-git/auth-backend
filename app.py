from flask import Flask
from flask_cors import CORS
from routes.auth_routes import auth_bp
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Flask app
app = Flask(__name__)

# Enable CORS dynamically from .env
FRONTEND_URL = os.getenv("FRONTEND_URL")
CORS(app, origins=[FRONTEND_URL])

# MongoDB configuration from .env
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

if not MONGO_URI:
    raise ValueError("MONGO_URI not set in .env file")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
app.db = db

# Register routes
app.register_blueprint(auth_bp, url_prefix="/api")

if __name__ == "__main__":
    # Flask host, port, debug mode from .env
    HOST = os.getenv("FLASK_HOST")
    PORT = int(os.getenv("FLASK_PORT"))
    DEBUG = os.getenv("FLASK_DEBUG", "True").lower() == "true"

    app.run(host=HOST, port=PORT, debug=DEBUG)
