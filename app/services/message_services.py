from app import producer, consumer
from kafka import KafkaConsumer
from kafka import KafkaProducer

import logging
logger = logging.getLogger(__name__)

# ===============
# Kakfa
# ===============

def initConsumer(consumer, topic, bootstrapServers):
  if(consumer == None):
    try:
      consumer = KafkaConsumer(topic, bootstrap_servers=boostrapServers)
      logger.info("Consumer Created")
    except Exception, e:
      logger.error(str(e))
  return consumer

def initProducer(producer, topic, boostrapServers):
  if(producer == None):
    try:
      producer = KafkaProducer(bootstrap_servers=bootstrapServers)
      logger.info("Producer Created")
    except Exception, e:
      logger.error(str(e))
  return producer

def consumeMessages():
    for message in consumer:
        # message value and key are raw bytes -- decode if necessary!
        # e.g., for unicode: `message.value.decode('utf-8')`
        print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                             message.offset, message.key,
                                             message.value))
        
def produceMessage(topic, key, message):
    producer.send(topic, { key : message})
