class Token(object):

	def __init__(self, username, password, date):
		self.username = username
		self.password = password
		self.date = date

	def to_string(self):
		return self.username + ':' + self.password

	def get_date(self):
		return self.date
