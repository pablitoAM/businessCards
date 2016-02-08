# ===============
#  User
# ===============

class User(object):

	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.counter = 0
		self.active = True



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

