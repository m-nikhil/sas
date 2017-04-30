from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

#Naming convention - full forms with '_' between each wor

class Batch(UserMixin,db.Model):

		__tablename__ = "batch"

		batch_id = db.Column(db.String(30),primary_key=True)

		#advisor
		ssk_advisor_id = db.Column(db.String(30),db.ForeignKey('advisor.employee_id'))
		verbal_advisor_id = db.Column(db.String(30),db.ForeignKey('advisor.employee_id'))
		aptitude_advisor_id = db.Column(db.String(30),db.ForeignKey('advisor.employee_id'))

		#relations
		student = db.relationship('Students',backref="batch",lazy="dynamic")



