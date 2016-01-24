from flask import Flask,jsonify
from flaskext.couchdb import CouchDBManager

app = Flask(__name__)
app.config.from_object('app.config')

print(app.config)

# ===============
# Database
# ===============

def getCouchDB(instance, app):
	if(instance == None):
		db_instance = CouchDBManager()
		db_instance.setup(app)
	return db_instance

couchdb = getCouchDB(None, app)

# ===============
# Imports
# ===============
from app.routes import auth_controller, print_controller, user_controller, error_controller
