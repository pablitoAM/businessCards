import json
from app import app, producer, consumer
from app.services import message_services

# ==============
# Print
# ==============

PREFIX = '/print'

# Print New Labels
@app.route(PREFIX + '/new/<int:number>', methods = ['POST'])
def print_new(number):
	data = request.get_data()
	print data;
	return json.dump(app)

# Print Existing Labels
@app.route(PREFIX + '/existing/<int:start_number>/<int:end_number>', methods = ['POST'])
def print_existing(start_number, end_number):
	data = request.get_data()
	print data;
	return json.dump(app)


# Test
@app.route(PREFIX, methods = ['GET'])
def test_send():
	message_services.produceMessage('Test', 'test-key', 'test-message')

