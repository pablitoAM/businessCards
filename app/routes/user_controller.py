import json
from app import app
from app.model.exception import JsonException
from app.services import user_services
from app.routes.secured import authenticate
# ==============
# User
# ==============

PREFIX = '/user'

# List of users
@app.route(PREFIX + '/list')
#@authenticate
def list():	
	return json.dumps(dict(result=user_services.list()))

# View User if exists
@app.route(PREFIX + '/view/<username>')
#@authenticate
def view(username):
	return json.dumps(dict(result=user_services.view(username)))

# Create User
@app.route(PREFIX + '/create', methods = ['POST'])
#@authenticate
def create():
	#verify data
	data = request.get_data()
	print data;
	return json.dumps(dict(result=user_services.create(data)))

# Update User
@app.route(PREFIX + '/update/<username>', methods = ['POST'])
@authenticate
def update(username):
	#verify data
	data = request.get_data()
	print data;
	return json.dumps(dict(result=user_services.update(username, data)))

# Delete User
@app.route(PREFIX + '/delete/<username>', methods = ['POST'])
#@authenticate
def delete(username):	
	return json.dumps(dict(result=user_services.delete(username)))


@app.route(PREFIX + '/setdata')
def setData():
	user_services.setRandomData()