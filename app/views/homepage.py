# homepage.py
from flask import Blueprint, render_template, session
from jinja2 import TemplateNotFound

homepage = Blueprint('homepage', __name__, template_folder='templates')

# A list of posts to display on the home page
# posts = [
#     {
#         "title": "Hello, Flask!   Evelyn was here!!",
#         "content": "This is my first post using Flask and Jinja."
#     },
#     {
#         "title": "Flask is awesome",
#         "content": "I'm learning how to use Flask to create web applications."
#     },
#     {
#         "title": "Flask templates",
#         "content": "Flask templates are easy to use and powerful."
#     }
# ]

@homepage.route('/')
def index():
    # Check if the user is logged in
    if 'email' in session:
        # print("user logged in")
        # print("session:", session)
        logged_in_user = session['email']
        return render_template('index.html', title='Home', username=logged_in_user)
    else:
        # Handle case when no user is logged in
        # print("no user logged in")
        return render_template('index.html', title='Home')