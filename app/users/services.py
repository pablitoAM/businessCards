from app.model.user import * 
from app.model.exception import JsonException
from app import mongo

# ===============
# User Services
# ===============

# List Users
def list():
	print mongo.db.user.find({'active' : True})

# Find User
def find(username):
	return mongo.db.user.find({'username': username})

# Check User
def check(username, password):
	return mongo.db.user.find({'$and' :[{'username': username}, {'password': password}]})

# Create User
def create(data):	
	if username in data and password in data:		
		user = find(data.username)
		if user == None:
			mongo.db.user.insert_one(data)
		else:
			raise JsonException(602, 'User with username ' +user.username+ ' already exists.')
	else:
		raise JsonException(603, 'No username nor password received for the user creation.')
	return True

# Update User
def update(username, data):
	# finds the user 
	user = find(username)
	if user == None:
		raise JsonException(601, 'User '+username+' not found.')
	else:
		_merge(user, data)
		mongo.db.user.update({ '_id': user._id }, { '$set': {data} })
	return True

# Delete User
def delete(username):
	# finds the user
	user = find_user(username)
	if user == None:
		raise JsonException(601, 'User '+username+' not found.')
	else:		
		mongo.db.user.update({ '_id': user._id }, { '$set': {'active' : False} })
	return True

# Def
def setRandomData():
	print 'Services Mongo!! %s' % mongo
	mongo.db.user.insert_many([{'username': 'u' + str(i), 'password' : 'p' + str(i)} for i in range(10)])
	return True


# ===============
# Private Methods
# ===============

def _merge(user, data):
	if password in data:
		user.password = data.password
	if display_name in data:
		user.display_name = data.display_name
	if phone in data:
		user.phone = data.phone
	if email in data:
		user.email = data.email 
	if counter in data:
		user.counter = data.counter
	if active in data:
		user.active = data.active
	if projectId in data:
		user.projectId = data.projectId