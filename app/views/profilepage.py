# profilepage.py
from flask import Blueprint, render_template, session
from jinja2 import TemplateNotFound
import pymysql

profilepage = Blueprint('profilepage', __name__, template_folder='templates')

# # @profilepage.route("/profile/<username>")
# @profilepage.route("/profile")
# # def profile(username):
# def profile():
#     # Render the profile.html template with the username variable
#     # return render_template("profile.html", title='Profile', username=username)
#     return render_template("profile.html", title='Profile')

def get_db():
    return pymysql.connect(
        host='mysql01.cs.virginia.edu',
        user='nrt3xs',
        password='UVa107CS4750!',
        database='nrt3xs',
        cursorclass=pymysql.cursors.DictCursor
    )

@profilepage.route('/profile')
def profile():
    if 'email' in session:
        # print("user logged in")
        # print("session:", session)
        # logged_in_user = session['email']
        first_name = session['first_name']
        return render_template('profile.html', title='Profile', username=first_name)
    else:
        # print("no user logged in")
        return render_template('index.html', title='Home')
