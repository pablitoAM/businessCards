from app import app

# ==============
# Print
# ==============

PREFIX = '/user'

@app.route(PREFIX)
@app.route('/index')
def index():
    return "Hello, World!"