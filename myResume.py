from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    #return '<h1>Welcome to James first server. Thanks for checking it out.</h1>'
    return render_template('home.html')


@app.route('/courses')
def get_all_courses():
    courses = [
        ['MISY350', 'Introduction to web development', 'Covers concepts related to client side development including cascading style sheets and JavaScript. PREREQ: MISY225.'],
        ['MISY330','Introduction to databases', 'Covers the design and implementation of enterprise databases in the business environment. A networked setting and its effect on database management will be emphasized. PREREQ: MISY160 or CISC181.'],
        ['FINC311','Intoduction to finance', 'Introduces fundamental techniques and concepts related to the financial management of business firms. Topics include the time value of money, valuation, capital budgeting, working capital management, cost of capital, capital structure analysis, short and long term financing. PREREQ: ACCT207 and MATH201.']]
    return render_template('courses.html', courses=courses)


@app.route('/about')
def get_user():
    #return '<h1>hello %s your age is %d</h1>' % (name, 3)
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True);
