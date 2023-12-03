# homepage.py
from flask import Blueprint, render_template, request, redirect, url_for, session
from jinja2 import TemplateNotFound
import pymysql

homepage = Blueprint('homepage', __name__, template_folder='templates')

pictures = [

     {'id': 1, 'url': '../static/img/doglogo.png', 'alt': 'mammal', 'type': "Mammals"},
     {'id': 2, 'url': '../static/img/birdlogo.png', 'alt': 'bird', 'type': "Birds"},
     {'id': 3, 'url': '../static/img/reptilelogo.png', 'alt': 'reptile', 'type': "Reptiles"},
     {'id': 4, 'url': '../static/img/fishlogo.png', 'alt': 'fish', 'type': "Fish"}

]

def get_db():
    return pymysql.connect(
        host='mysql01.cs.virginia.edu',
        user='nrt3xs',
        password='UVa107CS4750!',
        database='nrt3xs',
        cursorclass=pymysql.cursors.DictCursor
    )

@homepage.route('/')
def index():
    try:
        if 'user' in session:
            # Assuming the user information is stored under the 'user' key
            user_info = session['user']
            first_name = user_info['first_name']
            return render_template('index.html', title='Home', username=first_name, pictures=pictures)
        else:
            return render_template('index.html', title='Home')
    except Exception as e:
        print(str(e))
        return render_template('index.html', title='Home', error='Whoops... something happened. Please login again.')
