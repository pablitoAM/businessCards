import json
from flask import Blueprint
from app.model.exception import JsonException, UnauthorizedException
errors = Blueprint('errors', __name__)

# 404 Error Handling
@errors.errorhandler(404)
def not_found(error):
	ex = JsonException(404, error.description)
	return json.dumps(ex.serialize())

# 405 Error Handling
@errors.errorhandler(405)
def not_allowed(error):
	ex = JsonException(405, error.description)
	return json.dumps(ex.serialize())

# 401 
@errors.errorhandler(UnauthorizedException)
def exception(ex):	
	return json.dumps(ex.serialize())

# Other Exception 
@errors.errorhandler(JsonException)
def exception(ex):	
	return json.dumps(ex.serialize())