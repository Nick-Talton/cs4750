# checkoutpage.py
from flask import Blueprint, render_template, session
from jinja2 import TemplateNotFound
import pymysql

checkoutpage = Blueprint('checkoutpage', __name__, template_folder='templates')

# @checkoutpage.route("/checkout")
# # def profile(username):
# def checkout():
#     # Render the profile.html template with the username variable
#     # return render_template("profile.html", title='Profile', username=username)
#     return render_template("checkout.html", title='Checkout')

def get_db():
    return pymysql.connect(
        host='mysql01.cs.virginia.edu',
        user='nrt3xs',
        password='UVa107CS4750!',
        database='nrt3xs',
        cursorclass=pymysql.cursors.DictCursor
    )

@checkoutpage.route('/checkout')
def checkout():
    if 'email' in session:
        # print("user logged in")
        # print("session:", session)
        # logged_in_user = session['email']
        first_name = session['first_name']
        session_user = session['user']
        return render_template('checkout.html', title='Checkout', username=first_name, user=session_user)
    else:
        # print("no user logged in")
        return render_template('index.html', title='Home')
