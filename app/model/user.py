from app import couchdb
from flaskext.couchdb import ViewDefinition, ViewResults, Document, TextField, IntegerField, LongField, BooleanField, Row

# ===============
#  User
# ===============

class User(Document):
	username = TextField()
	password = TextField()
	display_name = TextField()
	phone = TextField()
	email = TextField()
	counter = IntegerField(default=0)
	active = BooleanField(default=True)
	projectId = LongField()

	def serialize(self):
		return {
		'username': self.username, 
		'display_name': self.display_name,
		'phone': self.phone,
		'email': self.email,
		'counter': self.counter,
		'projectId': self.projectId,
		'active' : self.active
		}

		couchdb.add_document(User)

# ===============
# Views
# ===============

# Finds all the users
user_list = ViewDefinition('user', 'user_list', '''\
	function(doc) {    	
		emit(doc);       
	}''', wrapper=User)

# Finds the user with the given key
find_user = ViewDefinition('user', 'find_user', '''\
	function(doc) {
		if(doc.username){
			emit(doc.username, doc)
		}	
	}''')

# Counts the number of users with the given username
count_by_username = ViewDefinition('user', 'count_by_username', '''\
	function(doc) {
		if(doc.username){
			emit(doc.username, doc)
		}	
	}''', '''\
	function(keys, values) {
		var sum = 0;
			for(var idx in values) {
				sum = sum + values[idx];
		}
		return sum;
	}''', wrapper=Row)

couchdb.add_viewdef((user_list, find_user, count_by_username))
