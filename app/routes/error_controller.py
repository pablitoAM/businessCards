from app import app
from flask import jsonify
from app.model.exception import JsonException, UnauthorizedException

# 404 Error Handling
@app.errorhandler(404)
def not_found(error):
	ex = JsonException(404, error.description)
	return jsonify(ex.serialize())

# 405 Error Handling
@app.errorhandler(405)
def not_allowed(error):
	ex = JsonException(405, error.description)
	return jsonify(ex.serialize())

# 401 
@app.errorhandler(UnauthorizedException)
def exception(ex):	
	return jsonify(ex.serialize())

# Other Exception 
@app.errorhandler(JsonException)
def exception(ex):	
	return jsonify(ex.serialize())