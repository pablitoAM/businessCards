from app import app
from flask import jsonify
from app.model.exception import JsonException

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
	ex = JsonException(404, error.description)
	return jsonify(ex.serialize())

@app.errorhandler(405)
def not_allowed(error):
	ex = JsonException(405, error.description)
	return jsonify(ex.serialize())