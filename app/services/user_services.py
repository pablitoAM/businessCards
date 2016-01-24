from app import couchdb
from flaskext.couchdb import ViewDefinition, Row, ViewResults
from app.model.entities import User

# ===============
# User Services
# ===============

# List Users
def list():
	return user_list()

# View User
def view(username):
	return ''

# Create User
def create(data):
	# check if there is no user with the same username
	# insert the user	
	return ''

# Update User
def update(user, data):
	return ''

# Delete User
def delete(user):
	return ''

# ===============
# Views
# ===============

# Finds all the users
user_list = ViewDefinition('user', 'user_list', '''\
    function (doc) {    
        doc.User.forEach(function (user) {
            emit(user);
        });
    }''')

couchdb.add_viewdef(user_list)