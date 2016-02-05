import json
from app import app
from app.services import message_services

# ==============
# Print
# ==============

PREFIX = '/print'

@app.route(PREFIX + '/new/<int:number>', methods = ['POST'])
def print_new(number):
	data = request.get_data()
	print data;
	return json.dump(app)

@app.route(PREFIX, methods = ['GET'])
def test_send():
	message_services.produceMessage('Test', 'test-key', 'test-message')

