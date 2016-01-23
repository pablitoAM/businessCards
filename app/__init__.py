from flask import Flask,jsonify
from app import config

app = Flask(__name__)

# ===============
# Imports
# ===============
from app.routes import auth_controller, print_controller, user_controller, error_controller