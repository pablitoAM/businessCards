from app import app
from flask import jsonify
from app.services import user_services

# ==============
# User
# ==============

PREFIX = '/user'

# List of users
@app.route(PREFIX + '/list')
def list():
	return jsonify(user_services.list())

# View User if exists
@app.route(PREFIX + '/view/<username>')
def view(username):
	print username
	return jsonify(user_services.view(username))

# Create User
@app.route(PREFIX + '/create', methods = ['POST'])
def create():
	#verify data
	data = request.get_data()
	print data;
	return jsonify(user_services.create(data))

# Update User
@app.route(PREFIX + '/update/<username>', methods = ['POST'])
def update(username):
	#verify data
	data = request.get_data()
	print data;
	return jsonify(user_services.update(username, data))

# Delete User
@app.route(PREFIX + '/delete/<username>', methods = ['POST'])
def delete(username):	
	return jsonify(user_services.delete(username))