import json
from app import app

# ==============
# Print
# ==============

PREFIX = '/print'

@app.route(PREFIX + '/new/<int:number>', methods = ['POST'])
def print_new(number):
	data = request.get_data()
	print data;
	return json.dump(result=True)

