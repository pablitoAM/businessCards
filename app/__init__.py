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

consumer = None
producer = None

# Initialises the consumer
def initConsumer(topic, bootstrapServers):
  if(consumer == None):
    try:
      consumer = KafkaConsumer(topic, bootstrap_servers=boostrapServers)
      logger.info("Consumer Created")
    except Exception, e:
      logger.error(str(e))
  return consumer

# Initialises the producer
def initProducer(topic, boostrapServers):
  if(producer == None):
    try:
      producer = KafkaProducer(bootstrap_servers=bootstrapServers)
      logger.info("Producer Created")
    except Exception, e:
      logger.error(str(e))
  return producer

# ===============
# Imports
# ===============
from app.routes import auth_controller, print_controller, user_controller, error_controller