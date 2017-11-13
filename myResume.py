from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    #return '<h1>Welcome to James first server. Thanks for checking it out.</h1>'
    return render_template('home.html')


@app.route('/courses')
def get_all_songs():
    courses = [
        'MISY350: Introduction to web development',
        'MISY330: Introduction to databases',
        'FINC311: Intoduction to Finance'
    ]
    return render_template('courses.html', courses=courses)


@app.route('/about')
def get_user():
    #return '<h1>hello %s your age is %d</h1>' % (name, 3)
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True);
