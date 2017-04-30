from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

#Naming convention - full forms with '_' between each wor

#needs to be reviewed
class Feedback(UserMixin,db.Model):

		__tablename__ = "feedback"

		feedback_id = db.Column(db.Integer,primary_key=True, autoincrement=True )

		student_id = db.Column(db.String(30),db.ForeignKey('student.roll_number'),nullable=False)
		semester = db.Column(db.Integer,nullable=False)

		#form
		quantitive_ability_score = db.Column(db.Integer)
		quantitive_ability_feedback = db.Column(db.String(100))
		quantitive_ability_feedback_given_on = db.Column(db.DateTime)
		quantitive_ability_feedback_given_by = db.Column(db.String(30))

		verbal_ability_score = db.Column(db.Integer)
		verbal_ability_feedback = db.Column(db.String(100))
		verbal_ability_feedback_given_on = db.Column(db.DateTime)
		verbal_ability_feedback_given_by = db.Column(db.String(30))

		soft_skills_score = db.Column(db.Integer)
		soft_skills_feedback = db.Column(db.String(100))
		soft_skills_feeback_given_on = db.Column(db.DateTime)
		soft_skills_feeback_given_by = db.Column(db.String(30))

		mock_gd_1_topic = db.Column(db.String(30))
		mock_gd_1_rating = db.Column(db.Integer)
		mock_gd_1_feedback = db.Column(db.String(100))
		mock_gd_1_feedback_given_on = db.Column(db.DateTime)
		mock_gd_1_feedback_given_by = db.Column(db.String(30))

		mock_gd_2_topic = db.Column(db.String(30))
		mock_gd_2_rating = db.Column(db.DateTime)
		mock_gd_2_feedback = db.Column(db.String(100))
		mock_gd_2_feedback_given_on = db.Column(db.DateTime)
		mock_gd_2_feedback_given_by = db.Column(db.String(30))

		mock_interview_1_topic = db.Column(db.String(30))
		mock_interview_1_rating = db.Column(db.Integer)
		mock_interview_1_feedback = db.Column(db.String(100))
		mock_interview_1_feedback_given_on = db.Column(db.DateTime)
		mock_interview_1_feedback_given_by = db.Column(db.String(30))

		mock_interview_2_topic = db.Column(db.String(30))
		mock_interview_2_rating = db.Column(db.Integer)
		mock_interview_2_feedback = db.Column(db.String(100))
		mock_interview_2_feedback_given_on = db.Column(db.DateTime)
		mock_interview_2_feedback_given_by = db.Column(db.String(30))



