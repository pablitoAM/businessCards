from flask import Flask
from app.config import configure_app, init_database, init_kafka, init_timestamp_signer
from app.auth.controllers import auth
from app.users.controllers import users
from app.printing.controllers import printing
from app.main.controllers import errors
from app.config import mongo
from app.config import session

# ===============
# Initialization
# ===============
app = Flask(__name__)

configure_app(app)
init_database(app) 
session.init_app(app)
# init_kafka(app)
init_timestamp_signer(app)

# ===============
# Blueprints
# ===============
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(users, url_prefix='/user')
app.register_blueprint(printing, url_prefix='/print')
app.register_blueprint(errors, url_prefix='/')
