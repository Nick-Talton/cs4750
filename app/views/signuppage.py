# signup.py
from flask import Blueprint, render_template, request, redirect, url_for, session
from jinja2 import TemplateNotFound
import pymysql
import bcrypt #youll need to pip install this btw, added to requirements

signuppage = Blueprint('signuppage', __name__, template_folder='templates')

def get_db():
    return pymysql.connect(
        host='mysql01.cs.virginia.edu',
        user='nrt3xs',
        password='UVa107CS4750!',
        database='nrt3xs',
        cursorclass=pymysql.cursors.DictCursor
    )

@signuppage.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        firstName = request.form.get("firstName")
        lastName = request.form.get("lastName")
        email = request.form.get("email")
        password = request.form.get("password")

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        with get_db() as connection:
            with connection.cursor() as cursor:
                #User does take an additional optional field address_id where we can add it in a profile edit or it doesnt really matter tbh
                # paramertized queries
                query = "INSERT INTO Users (email, password, first_name, last_name) VALUES (%s, %s, %s, %s)"
                cursor.execute(query, (email, hashed_password, firstName, lastName))
                connection.commit()
        
        with get_db() as connection:
            with connection.cursor() as cursor:
                query = "SELECT * FROM Users WHERE email=%s"
                cursor.execute(query, (email,))
                user = cursor.fetchone()

                if user and (hashed_password == user['password']):
                    session['user'] = user
        
        session['email'] = email
        session['first_name'] = firstName

        #print(session)

        return render_template('index.html', username=firstName)

    return render_template("signup.html")