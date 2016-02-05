import json
from flask import Flask,jsonify,session
from flaskext.couchdb import CouchDBManager
from flask.ext.session import Session

app = Flask(__name__)
app.config.from_object('app.config')

# ===============
# Session
# ===============

sess = Session()
sess.init_app(app)

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
# Kafka
# ===============
boostrapServers = app.config['BOOTSTRAP_SERVERS']
topic = app.config['MESSAGE_TOPIC']

producer = None
consumer = None

from app.services.message_services import initConsumer, initProducer
initProducer(producer, topic, boostrapServers)
initConsumer(consumer, topic, boostrapServers)

# ===============
# Imports
# ===============
from app.routes import auth_controller, print_controller, user_controller, error_controller