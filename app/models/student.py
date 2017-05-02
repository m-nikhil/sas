from app import db

#Naming convention - full forms with '_' between each words

class Student(db.Model):

		__tablename__ = 'student'

		#personal
		roll_number = db.Column(db.String(30),db.ForeignKey('login_credentials_student.id'),primary_key=True)
		name = db.Column(db.String(30),nullable=False)
		email_id = db.Column(db.String(30),nullable=False,unique=True)
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
