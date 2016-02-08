# ===============
# Label
# ===============

class TagSerial(object):

	def __init__(self, username, companyCode, product, nextSerial):
		self.username = username
		self.companyCode = companyCode
		self.product = product
		self.nextSerial = nextSerial

	def serialize(self):
		return {
		'username': self.username,
		'companyCode' : self.companyCode,
		'product' : self.product,
		'nextSerial' : self.nextSerial
		}