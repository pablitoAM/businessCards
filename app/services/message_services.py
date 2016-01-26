import logging
from kafka import KafkaConsumer
from kafka import KafkaProducer

# ===============
# Kakfa
# ===============    
producer = None
consumer = None

def initConsumer(topic, bootstrapServers):
  if(consumer == None):
    try:
      consumer = KafkaConsumer(topic, bootstrap_servers=boostrapServers)
    except Exception, e:
      logger.error(str(e))
  return consumer

def initProducer(topic, boostrapServers):
  if(producer == None):
    try:
      producer = KafkaProducer(bootstrap_servers=bootstrapServers)
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
