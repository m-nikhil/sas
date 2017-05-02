from app import db

#Naming convention - full forms with '_' between each word

class Advisor(db.Model):

		__tablename__ = 'advisor'

		#personal
		employee_id = db.Column(db.String(30),db.ForeignKey('login_credentials_lecturer.id'),primary_key=True)
		name = db.Column(db.String(30),nullable=False)
		email_id = db.Column(db.String(30),nullable=False,unique=True)
		contact_number = db.Column(db.Integer)
		address = db.Column(db.String(50))
		date_of_birth = db.Column(db.DateTime)

		#relationship
		ssk_advisor_batch = db.relationship('Batch',foreign_keys='Batch.ssk_advisor_id',backref="ssk_advisor",lazy="dynamic")
		verbal_advisor_batch = db.relationship('Batch',foreign_keys='Batch.verbal_advisor_id',backref="verbal_advisor",lazy="dynamic")
		aptitude_advisor_batch = db.relationship('Batch',foreign_keys='Batch.aptitude_advisor_id',backref="aptitude_advisor",lazy="dynamic")


		