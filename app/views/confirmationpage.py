# confirmationpage.py
from flask import Blueprint, render_template
from jinja2 import TemplateNotFound

confirmationpage = Blueprint('confirmationpage', __name__, template_folder='templates')

@confirmationpage.route("/confirmation")
# def profile(username):
def confirmation():
    # Render the profile.html template with the username variable
    # return render_template("profile.html", title='Profile', username=username)
    return render_template("confirmation.html", title='Confirmation')

