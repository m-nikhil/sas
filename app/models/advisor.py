from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

#Naming convention - full forms with '_' between each wor

class Advisor(UserMixin,db.Model):

		__tablename__ = 'advisor'

		#personal
		employee_id = db.Column(db.String(30),primary_key=True,index = True)
		password_hash = db.Column(db.String(300),nullable=False)
		name = db.Column(db.String(30),nullable=False)
		active = db.Column(db.Boolean, nullable=False, default=True)
		email_id = db.Column(db.String(30),nullable=False)
		contact_number = db.Column(db.Integer)
		address = db.Column(db.String(50))
		date_of_birth = db.Column(db.DateTime)

		#admin or not
		role = db.Column(db.String(300),nullable=False)

		#relationship
		ssk_advisor_batch = db.relationship('Batch',foreign_keys='Batch.ssk_advisor_id',backref="ssk_advisor",lazy="dynamic")
		verbal_advisor_batch = db.relationship('Batch',foreign_keys='Batch.verbal_advisor_id',backref="verbal_advisor",lazy="dynamic")
		aptitude_advisor_batch = db.relationship('Batch',foreign_keys='Batch.aptitude_advisor_id',backref="aptitude_advisor",lazy="dynamic")


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