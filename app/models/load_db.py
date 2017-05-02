from app import db
from login_credentials_lecturer import Login_credentials_lecturer
from login_credentials_student import Login_credentials_student
from student import Student
from advisor import Advisor
from batch import Batch
from feedback import Feedback


#preserve the order of classes loaded

def load_db(db):

	db.drop_all()
	db.create_all()

	#login_credentials_lecturer
	lec_1 = Login_credentials_lecturer(id="lec_1",password_hash="123")
	lec_2 = Login_credentials_lecturer(id="lec_2",password_hash="123",role="verbal")
	lec_3 = Login_credentials_lecturer(id="lec_3",password_hash="123",role="aptitude")
	lec_4 = Login_credentials_lecturer(id="lec_4",password_hash="123",role="admin")
	db.session.add(lec_1)
	db.session.add(lec_2)
	db.session.add(lec_3)
	db.session.add(lec_4)

	db.session.commit()

	#login_credentials_student
	stu_1 = Login_credentials_student(id="CB.EN.U4CSE14132",password_hash="nik@1996")
	stu_2 = Login_credentials_student(id="CB.EN.U4CSE14600",password_hash="123")
	db.session.add(stu_1)
	db.session.add(stu_2)

	db.session.commit()


	#advisor
	e1 = Advisor(employee_id="lec_1",name="employee_1",email_id="employee_1@gmail.com") 
	e2 = Advisor(employee_id="lec_2",name="employee_2",email_id="employee_2@gmail.com")
	e3 = Advisor(employee_id="lec_3",name="employee_3",email_id="employee_3@gmail.com")
	e4 = Advisor(employee_id="lec_4",name="employee_4",email_id="employee_4@gmail.com")
	db.session.add(e1)
	db.session.add(e2)
	db.session.add(e3)
	db.session.add(e4)

	db.session.commit()
	
	#batch
	b1 = Batch(batch_id = "b1",ssk_advisor_id = "lec_1",verbal_advisor_id="lec_2", aptitude_advisor_id="lec_3")
	b2 = Batch(batch_id = "b2",ssk_advisor=e1,verbal_advisor=e2, aptitude_advisor=e3) 
	db.session.add(b1)
	db.session.add(b2)

	db.session.commit()

	#student
	s1 = Student(roll_number="CB.EN.U4CSE14132",name="nikhil",email_id="m@nikhil@outlook.com",batch_id="b1")
	s2 = Student(roll_number="CB.EN.U4CSE14600",name="name_600",email_id="name_600@amrita.com",batch = b2)      
	db.session.add(s1)
	db.session.add(s2)

	db.session.commit()

	#feedback
	f1 = Feedback(student_id = "CB.EN.U4CSE14132", semester = "1")
	f2 = Feedback(student_id = "CB.EN.U4CSE14132", semester = "2")
	f3 = Feedback(student_id = "CB.EN.U4CSE14600", semester = "1")

	db.session.add(f1)
	db.session.add(f2)
	db.session.add(f3)

	db.session.commit()
