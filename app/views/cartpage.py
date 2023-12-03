# cartpage.py
from flask import Blueprint, render_template, session
from jinja2 import TemplateNotFound
import pymysql

cartpage = Blueprint('cartpage', __name__, template_folder='templates')

def get_db():
    return pymysql.connect(
        host='mysql01.cs.virginia.edu',
        user='nrt3xs',
        password='UVa107CS4750!',
        database='nrt3xs',
        cursorclass=pymysql.cursors.DictCursor
    )

@cartpage.route('/cart')
def cart():
    if 'email' in session:
        # print("user logged in")
        # print("session:", session)
        # logged_in_user = session['email']
        first_name = session['first_name']
        return render_template('cart.html', title='Shopping Cart', username=first_name)
    else:
        # print("no user logged in")
        return render_template('index.html', title='Home')


# @cartpage.route('/cart')
# def cart():
#     # render the shopping cart template
#     return render_template('cart.html', title='Shopping Cart')