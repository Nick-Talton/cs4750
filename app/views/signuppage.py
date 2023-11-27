# signup.py
from flask import Blueprint, render_template, request
from jinja2 import TemplateNotFound

signuppage = Blueprint('signuppage', __name__, template_folder='templates')

@signuppage.route("/signup", methods=["GET", "POST"])
def signup():
    # If the request method is POST, get the form data and redirect to the profile page
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # You can add your own logic to validate the username and password here
        return redirect(url_for("profile", title='Signup', username=username))
    # If the request method is GET, render the signup.html template
    return render_template("signup.html")