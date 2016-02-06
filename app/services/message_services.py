from kafka import KafkaConsumer
from kafka import KafkaProducer

import logging
logger = logging.getLogger(__name__)

# ===============
# Kakfa
# ===============

def consumeMessages(consumer):
    initConsumer()
    for message in consumer:
        # message value and key are raw bytes -- decode if necessary!
        # e.g., for unicode: `message.value.decode('utf-8')`
        print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                             message.offset, message.key,
                                             message.value))
        
def produceMessage(producer, topic, key, message):
    initProducer()
    producer.send(topic, { key : message})
