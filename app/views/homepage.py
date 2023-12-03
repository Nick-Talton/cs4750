# homepage.py
from flask import Blueprint, render_template, request, redirect, url_for, session
from jinja2 import TemplateNotFound
import pymysql

homepage = Blueprint('homepage', __name__, template_folder='templates')

def get_db():
    return pymysql.connect(
        host='mysql01.cs.virginia.edu',
        user='nrt3xs',
        password='UVa107CS4750!',
        database='nrt3xs',
        cursorclass=pymysql.cursors.DictCursor
    )

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
    try:
        if 'email' in session:
            # print("user logged in")
            # print("session:", session)
            # logged_in_user = session['email']
            first_name = session['first_name']
            return render_template('index.html', title='Home', username=first_name, error='Whoops... something happened. Please login again.')
        else:
            # print("no user logged in")
            return render_template('index.html', title='Home')
    except:
        return render_template('index.html', title='Home', error='Whoops... something happened. Please login again.')