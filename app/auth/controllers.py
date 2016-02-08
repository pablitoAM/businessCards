import json
from app.users import services as user_services
import services as auth_services
from flask import Blueprint, request
auth = Blueprint('auth', __name__)

# ==============
# Login
# ==============
@auth.route('/login', methods = ['POST'])
def login():	
	username = request.form['username']
	password = request.form['password']
	if user_services.check(username,password):
		token = auth_services.create_token(username, password)
		print token
		return json.dumps(token)		

@auth.route('/logout', methods = ['GET'])
def logout():
    return json.dumps(True)
