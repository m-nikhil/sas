from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

#Naming convention - full forms with '_' between each word

class Login_credentials_lecturer(UserMixin,db.Model):

		__tablename__ = 'login_credentials_lecturer'

		id = db.Column(db.String(30),primary_key=True,index = True)
		password_hash = db.Column(db.String(300),nullable=False)
		active = db.Column(db.Boolean, nullable=False, default=True)

		role = db.Column(db.Enum('admin','verbal','ssk','aptitude'),default = 'ssk')

		@property
		def password(self):
			"""
			Prevent pasword from being access
			"""
			raise AttributeError('password is not a readable attribute.')

  		@password.setter
  		def password(self, password):
  			"""
  			Set password to a hashed password
  			"""
  			self.password_hash = generate_password_hash(password)


		def verify_password(self, password):
			"""
			Check if hashed password matches actual password
			"""
			return check_password_hash(self.password_hash, password)
