import json
from flask import Blueprint
auth = Blueprint('auth', __name__)

# ==============
# Login
# ==============
@auth.route('/login', methods = ['POST'])
def login():
	data = request.get_data()
	# check credentials
	# store credentials in session
	print data;
	return json.dumps(result=data)

@auth.route('/logout', methods = ['GET'])
def logout():
    return json.dumps(True)