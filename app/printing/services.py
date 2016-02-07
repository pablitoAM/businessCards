from app.model.tag_serial import TagSerial
from app.config import producer, consumer

# Consume messages
def consumeMessages():
    for message in consumer:
        # message value and key are raw bytes -- decode if necessary!
        # e.g., for unicode: `message.value.decode('utf-8')`
        print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                             message.offset, message.key,
                                             message.value))
# Produce Messages        
def produceMessage(topic, key, message):
    producer.send(topic, { key : message})

# Print New Labels
def print_new():
	return None
