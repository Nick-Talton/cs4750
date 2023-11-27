# confirmationpage.py
from flask import Blueprint, render_template
from jinja2 import TemplateNotFound

postconfirmationpage = Blueprint('postconfirmationpage', __name__, template_folder='templates')

@postconfirmationpage.route("/postconfirmation")
# def profile(username):
def postconfirmation():
    # Render the profile.html template with the username variable
    # return render_template("profile.html", title='Profile', username=username)
    return render_template("postconfirmation.html", title='Postconfirmation')

