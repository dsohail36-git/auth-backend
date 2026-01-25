# from flask import Flask, request, jsonify
# from flask_cors import CORS 
# from routes.auth_routes import auth_bp
# from pymongo import MongoClient

# from pathlib import Path

# app = Flask(__name__)

# # Fix: Enable CORS only for frontend origin
# CORS(app, origins=["http://localhost:3000"])

# # Fix: Properly setup MongoDB connection and assign db to app.db for access in routes
# client = MongoClient("mongodb://localhost:27017/")
# db = client['Authentication'] 
# app.db = db

# # Fix: Register blueprint with '/api' prefix so React calls to /api/login will work
# app.register_blueprint(auth_bp, url_prefix="/api")

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5001, debug=True)


from flask import Flask, request, jsonify
from flask_cors import CORS 
from routes.auth_routes import auth_bp
from pymongo import MongoClient
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Enable CORS (local React frontend)
CORS(app, origins=["http://localhost:3000"])

load_dotenv()
# ✅ Use environment variable for MongoDB
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)

db = client["Authentication"]
app.db = db

app.register_blueprint(auth_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
