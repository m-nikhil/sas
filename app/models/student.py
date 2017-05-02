from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

#Naming convention - full forms with '_' between each words

class Student(UserMixin,db.Model):

		__tablename__ = 'student'

		#personal
		roll_number = db.Column(db.String(30),primary_key=True, index=True)
		password_hash = db.Column(db.String(300),nullable=False)
		name = db.Column(db.String(30),nullable=False)
		active = db.Column(db.Boolean, nullable=False, default=True)
		email_id = db.Column(db.String(30),unique=True)
		contact_number = db.Column(db.Integer)
		address = db.Column(db.String(50))
		date_of_birth = db.Column(db.DateTime)

		#batch
		batch_id = db.Column(db.String(30),db.ForeignKey('batch.batch_id'))

		#academics
		specialization_ug = db.Column(db.String(30))
		institution_ug = db.Column(db.String(30))
		degree_ug = db.Column(db.String(30))
		cgpa_ug = db.Column(db.Float)
		specialization_12 = db.Column(db.String(30))
		institution_12 = db.Column(db.String(30))
		board_12 = db.Column(db.String(30))
		marks_12 = db.Column(db.Integer)
		specialization_10 = db.Column(db.String(30))
		institution_10 = db.Column(db.String(30))
		board_10 = db.Column(db.String(30))
		marks_10 = db.Column(db.Integer)

		#others
		resume = db.Column(db.Text)
		career_goals = db.Column(db.Text)
		achievements = db.Column(db.Text)
		photo = db.Column(db.LargeBinary)

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



# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return Student.query.get(roll_number)
