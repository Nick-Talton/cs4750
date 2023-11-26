from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

# A list of posts to display on the home page
posts = [
    {
        "title": "Hello, Flask!",
        "content": "This is my first post using Flask and Jinja."
    },
    {
        "title": "Flask is awesome",
        "content": "I'm learning how to use Flask to create web applications."
    },
    {
        "title": "Flask templates",
        "content": "Flask templates are easy to use and powerful."
    }
]

# A list of users to display on the search results page
users = [
    {
        "username": "alice",
        "bio": "I love Flask and Python."
    },
    {
        "username": "bob",
        "bio": "I'm a beginner in web development."
    },
    {
        "username": "charlie",
        "bio": "I'm a fan of open source software."
    }
]

def get_db():
    return pymysql.connect(host='mysql01.cs.virginia.edu',
                           user='nrt3xs',
                           password='UVa107CS4750!',
                           database='nrt3xs',
                           cursorclass=pymysql.cursors.DictCursor)

@app.route('/')
def index():
    # Render the index.html template with the posts variable
    return render_template("index.html", title='Home', posts=posts)

@app.route('/login')
def login():
    # render the login template
    return render_template('login.html', title='Login')

@app.route('/cart')
def cart():
    # render the shopping cart template
    return render_template('cart.html', title='Shopping Cart')

@app.route('/post/<int:id>')
def post(id):
    # render the post template with the given id
    return render_template('post.html', title='Post', id=id)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    # If the request method is POST, get the form data and redirect to the profile page
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # You can add your own logic to validate the username and password here
        return redirect(url_for("profile", title='Signup', username=username))
    # If the request method is GET, render the signup.html template
    return render_template("signup.html")

@app.route("/profile/<username>")
def profile(username):
    # Render the profile.html template with the username variable
    return render_template("profile.html", title='Profile', username=username)

@app.route("/create")
def create():
    # Render the create.html template
    return render_template("create.html", title='Create')

@app.route("/search", methods=["GET", "POST"])
def search():
    # If the request method is POST, get the query and filter the users list
    if request.method == "POST":
        query = request.form.get("query")
        # You can use your own logic to search for users here
        results = [user for user in users if query.lower() in user["username"].lower()]
        # Render the results.html template with the query and results variables
        return render_template("results.html", query=query, results=results)
    # If the request method is GET, render the search.html template
    return render_template("search.html", title='Search')

@app.route("/appointment", methods=["GET", "POST"])
def appointment():
    # If the request method is POST, get the form data and redirect to the confirmation page
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        date = request.form.get("date")
        time = request.form.get("time")
        # You can add your own logic to save the appointment data here
        return redirect(url_for("confirmation", name=name, date=date, time=time))
    # If the request method is GET, render the appointment.html template
    return render_template("appointment.html", title='Create Appointment')

@app.route("/confirmation/<name>/<date>/<time>")
def confirmation(name, date, time):
    # Render the confirmation.html template with the name, date, and time variables
    return render_template("confirmation.html", name=name, date=date, time=time, title='Confirmation')

if __name__ == '__main__':
    app.run(debug=True)


