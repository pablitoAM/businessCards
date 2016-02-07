import json
import services as printing_services
from flask import Blueprint, request
printing = Blueprint('printing', __name__)
from app.users import services as user_services

# ==============
# Print
# ==============

# Print New Labels
@printing.route('/new/<int:number>', methods = ['POST'])
def print_new(number):
	data = request.get_json()
	print data
	print request.get_data()
	#data = json.loads(request.form)
	print request.values
	return json.dumps(data)

# Print Existing Labels
@printing.route('/existing/<int:start_number>/<int:end_number>', methods = ['POST'])
def print_existing(start_number, end_number):
	data = request.get_data()
	print data;
	return json.dumps(data)


# Test
@printing.route('/', methods = ['GET'])
def test_send():	
	printing_services.produceMessage('Test', 'test-key', 'test-message')

