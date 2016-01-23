# ===============
# JSON Exception
# ===============

class JsonException:

	# Constructor
	def __init__(self, code, message):
		self.code = code
		self.message = message

	def serialize(self):  
		return {           
			'code': self.code, 
			'message': self.message
		}