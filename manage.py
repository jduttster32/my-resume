from flask_script import Manager
from myResume import app, db, Teacher, Course

manager = Manager(app)

@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    teacher1 = Teacher(name='Hao Jiang', department='ECON')
    teacher2 = Teacher(name='Christopher Lynch', department='FINC')
    teacher3 = Teacher(name='Charles Cotton', department='MIS')
    course1 = Course(number='308', name='Banking and Monetary Policy', description='Nature and economic significance of money, credit and the banking system; the origin and management of the money supply; and effects of monetary changes on price levels, output and employment. PREREQ: ECON103.', teacher=teacher1)
    course2 = Course(number='311', name='Principles of Finance', description='Introduces fundamental techniques and concepts related to the financial management of business firms. Topics include the time value of money, valuation, capital budgeting, working capital management, cost of capital, capital structure analysis, short and long term financing. PREREQ: ACCT207 and MATH201. PREREQ for HRIM majors: ACCT207 and MATH201 or STAT200. RESTRICTIONS: Not open to Freshmen. Open to students whose major requires this course.', teacher=teacher2)
    course3 = Course(number='465', name='Introduction to CyberSecurity', description='This cybersecurity course is an introduction to computer and network security and covers the foundation security policies and methods to provide confidentiality, integrity, and availability, as well as cryptography, auditing, and user security. Topics are reinforced with hands-on exercises run in a virtual machine environment.')
    course4 = Course(number='225', name='Introduction to Java Programming', description='Use of higher level contemporary computing languages to structure Prototyping applications of systems. PREREQ: MISY160 or CISC101. RESTRICTIONS: Not open to CIS majors in the MIS minor.')
    db.session.add(teacher1)
    db.session.add(teacher2)
    db.session.add(course1)
    db.session.add(course2)
    db.session.add(course3)
    db.session.add(course4)
    db.session.commit()

if __name__ == '__main__':
    manager.run()
