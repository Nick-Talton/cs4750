import sys
sys.path.append("views")

from flask import Flask, render_template, request, redirect, url_for
from homepage import homepage
from loginpage import loginpage
from signuppage import signuppage
from appointmentpages import appointmentpages
from cartpage import cartpage
from postspages import postspages
from profilepage import profilepage
from searchpage import searchpage
import pymysql

app = Flask(__name__)

def get_db():
    return pymysql.connect(host='mysql01.cs.virginia.edu',
                           user='nrt3xs',
                           password='UVa107CS4750!',
                           database='nrt3xs',
                           cursorclass=pymysql.cursors.DictCursor)

app.register_blueprint(homepage) # /
app.register_blueprint(loginpage) # /login
app.register_blueprint(signuppage) # /signup
app.register_blueprint(appointmentpages) # /appointment and /appointment/confirmation/<name>/<date>/<time>
app.register_blueprint(cartpage) # /cart
app.register_blueprint(postspages) # /post/create and /post/<int:id>
app.register_blueprint(profilepage) # /profile/<user>
app.register_blueprint(searchpage) # /searchpage

