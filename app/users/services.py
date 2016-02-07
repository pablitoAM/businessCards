from flaskext.couchdb import ViewResults
from app.config import database
from app.model.user import * 
from app.model.exception import JsonException

# ===============
# User Services
# ===============

# List Users
def list():
	results = user_list()
	return_list = []
	if results.total_rows > 0:
		for user in results.rows:
			return_list.append(user.serialize())
	return return_list

# View User
def view(username):
	return find_user(username)

# Create User
def create(data):
	if username in data and password in data:		
		user = count_by_username(data)
		if user == None:
			user = User(username=data.username, password = data.password)
			_merge(user, data)
			user.store()
		else:
			raise JsonException(602, 'User with username ' +user.username+ ' already exists.')
	else:
		raise JsonException(603, 'No username nor password received for the user creation.')

	return True

# Update User
def update(username, data):
	# finds the user 
	user = find_user(username)
	if(user == None):
		raise JsonException(601, 'User '+username+' not found.')
	else:
		_merge(user, data)				
		user.store()
	return True

# Delete User
def delete(username):
	# finds the user
	user = find_user(username)
	if(user == None):
		raise JsonException(601, 'User '+username+' not found.')
	else:
		user.active = False
		user.store()
	return True

# Def
def setRandomData():
	for i in range(10):
		user = User(username='u' + str(i), password='p' + str(i))
		user.store()

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