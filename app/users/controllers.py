import json
from flask import Blueprint
import services as user_services
users = Blueprint('users', __name__)

# ==============
# User
# ==============

# List of users
@users.route('/list')
#@authenticate
def list():	
	return json.dumps(dict(result=user_services.list()))

# View User if exists
@users.route('/view/<username>')
#@authenticate
def view(username):
	return json.dumps(dict(result=user_services.view(username)))

# Create User
@users.route('/create', methods = ['POST'])
#@authenticate
def create():
	#verify data
	data = request.get_data()
	print data;
	return json.dumps(dict(result=user_services.create(data)))

# Update User
@users.route('/update/<username>', methods = ['POST'])
#@authenticate
def update(username):
	#verify data
	data = request.get_data()
	print data;
	return json.dumps(dict(result=user_services.update(username, data)))

# Delete User
@users.route('/delete/<username>', methods = ['POST'])
#@authenticate
def delete(username):	
	return json.dumps(dict(result=user_services.delete(username)))


@users.route('/setdata')
def setData():
	user_services.setRandomData()