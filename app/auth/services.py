from app.config import timestamp_signer as ts
from app.model.token import Token

# Creates a token for the given username
def create_token(username, password):
	token = ts.sign(username+':'+password)	
	return token

# Parses the token and extracts the data in a dict
def read_token(token):
	return None

# Checks if the token is valid against the current date
def is_valid_token(token):
	return None

# Refreshes the token in session and sends it back to the user
def refresh_token(token):
	return None