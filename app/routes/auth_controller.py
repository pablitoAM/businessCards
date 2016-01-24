from app import app
from flask import jsonify, request

# ==============
# Login
# ==============

PREFIX = '/auth'
@app.route(PREFIX + '/login', methods = ['POST'])
def login():
	data = request.get_data()
	print data;
	return jsonify(result=data)

@app.route(PREFIX + '/logout', methods = ['GET'])
def logout():
    return jsonify(result=True)