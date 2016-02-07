from app.config import database
from flaskext.couchdb import ViewDefinition, ViewResults, Document, TextField, IntegerField, LongField

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

database.add_document(TagSerial)