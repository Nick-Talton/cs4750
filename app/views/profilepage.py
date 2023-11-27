# profilepage.py
from flask import Blueprint, render_template
from jinja2 import TemplateNotFound

profilepage = Blueprint('profilepage', __name__, template_folder='templates')

# @profilepage.route("/profile/<username>")
@profilepage.route("/profile")
# def profile(username):
def profile():
    # Render the profile.html template with the username variable
    # return render_template("profile.html", title='Profile', username=username)
    return render_template("profile.html", title='Profile')

