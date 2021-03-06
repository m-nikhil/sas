#third party
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

#local imports
from config import app_config


#db initialization
db = SQLAlchemy()

#login manager initializations
login_manager = LoginManager()

def create_app(config_name):
	app = Flask(__name__,instance_relative_config=True)
	app.config.from_object(app_config[config_name])
    	app.config.from_pyfile('config.py')

	db.init_app(app)

	login_manager.init_app(app)
	login_manager.login_message = "You must be logged in to access this page."
	login_manager.login_view = "auth.login"

	migrate = Migrate(app, db)
	from models import student,advisor,feedback,batch

	#loading sample db
	
	if(config_name == "development"):
		with app.test_request_context():
			from models import load_db	
			load_db.load_db(db)

	@app.route('/')
    	def hello_world():
        	return 'Hello, World!'

	return app

