# loginpage.py
from flask import Blueprint, render_template
from jinja2 import TemplateNotFound

loginpage = Blueprint('login', __name__, template_folder='templates')

@loginpage.route('/login')
def login():
    # render the login template
    return render_template('login.html', title='Login')