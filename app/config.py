# configuration
import os
import logging

class BaseConfig(object):
    SECRET_KEY = 'development key'
    COUCHDB_SERVER = 'http://127.0.0.1:5984'
    COUCHDB_DATABASE = 'db_bs'
    #SESSION_COOKIE_NAME = 'bizCards'
    #SESSION_COOKIE_SECURE = True
    #PERMANENT_SESSION_LIFETIME = 600
    #SESSION_TYPE = 'filesystem'
    #SESSION_USE_SIGNER = True
    MESSAGE_TOPIC = 'businessCards'
    BOOTSTRAP_SERVERS = '127.0.0.1:9092'
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = 'businessCards.log'
    LOGGING_LEVEL = logging.INFO

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    SECRET_KEY = 'development key'
    LOGGING_LOCATION = 'businessCards_debug.log'
    LOGGING_LEVEL = logging.DEBUG

class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    SECRET_KEY = 'test key'
    LOGGING_LOCATION = 'businessCards_test.log'
    LOGGING_LEVEL = logging.DEBUG

config = {
    "development": "app.config.DevelopmentConfig",
    "testing": "app.config.TestingConfig",
    "default": "app.config.DevelopmentConfig"
}

def configure_app(app):
    config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    app.config.from_object(config[config_name])    

    # Configure logging
    handler = logging.FileHandler(app.config['LOGGING_LOCATION'])
    handler.setLevel(app.config['LOGGING_LEVEL'])
    formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

# ===============
# Database
# ===============
from flaskext.couchdb import CouchDBManager
database = CouchDBManager()

# ===============
# Session
# ===============
from flask.ext.session import Session
session = Session()

# ===============
# Kafka
# ===============
from kafka import KafkaConsumer
from kafka import KafkaProducer

consumer = None
producer = None

def init_kafka(app):

    boostrapServers = app.config['BOOTSTRAP_SERVERS']    
    topic = app.config['MESSAGE_TOPIC']
    app.logger.info("Initialising Kafka. Topic: %s Bootstrap Servers: %s", topic, boostrapServers)

    try:
        consumer = KafkaConsumer(topic, bootstrap_servers=boostrapServers)
        app.logger.info("Consumer Created")
    except Exception, e:
        app.logger.error('Exception creating consumer: %s', str(e))

    try:
        producer = KafkaProducer(bootstrap_servers=boostrapServers)
        app.logger.info("Producer Created")

    except Exception, e:
        app.logger.error('Exception creating producer: %s', str(e))