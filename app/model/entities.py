from app import couchdb
from flaskext.couchdb import Document, TextField, IntegerField, LongField

# ===============
#  User
# ===============

class User(Document):
	username = TextField()
	password = TextField()
	display_name = TextField()
	phone = TextField()
	email = TextField()
	counter = IntegerField()
	projectId = LongField()

	def serialize(self):
		return {
		'username': self.username, 
		'display_name': self.display_name,
		'phone': self.phone,
		'email': self.email,
		'counter': self.counter,
		'projectId': self.projectId
		}

couchdb.add_document(User)

# ===============
# Label
# ===============

class TagSerial(Document):
	username = TextField()
	companyCode = LongField()
	product = LongField()
	nextSerial = LongField()

	def serialize(self):
		return {
		'username': self.username,
		'companyCode' : self.companyCode,
		'product' : self.product,
		'nextSerial' : self.nextSerial
		}

couchdb.add_document(User)