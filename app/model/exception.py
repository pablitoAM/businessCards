# ===============
# JSON Exception
# ===============

class JsonException(Exception):

	# Constructor
	def __init__(self, code, message):
		Exception.__init__(self)
		self.code = code
		self.message = message

	def serialize(self):  
		return {           
			'code': self.code, 
			'message': self.message
		}

# ===============
# UnauthorizedException
# ===============
class UnauthorizedException(Exception):

	# Constructor
	def __init__(self, message):
		Exception.__init__(self)		
		self.code = 401
		self.message = message

	def serialize(self):  
		return {           
			'code': self.code, 
			'message': self.message
		}