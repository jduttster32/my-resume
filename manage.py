from flask_script import Manager
from myResume import app

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
