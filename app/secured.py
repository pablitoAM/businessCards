from functools import wraps
from flask import g, request, session
from app.model.exception import UnauthorizedException


def valid_credentials():	
	return 'USER' in session and 'PASS' in session


def authenticate(f):
	@wraps(f)
	def wrapper(*args, **kwargs):
		if (not valid_credentials()):
			raise UnauthorizedException('Authentication Required.')
		return f(*args, **kwargs)
	return wrapper
