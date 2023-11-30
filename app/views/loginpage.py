# loginpage.py
from flask import Blueprint, render_template, request, redirect, url_for, session
import pymysql

loginpage = Blueprint('login', __name__, template_folder='templates')

def get_db():
    return pymysql.connect(
        host='mysql01.cs.virginia.edu',
        user='nrt3xs',
        password='UVa107CS4750!',
        database='nrt3xs',
        cursorclass=pymysql.cursors.DictCursor
    )

@loginpage.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        with get_db() as connection:
            with connection.cursor() as cursor:
                query = "SELECT * FROM Users WHERE email=%s AND password=%s"
                cursor.execute(query, (email, password))
                user = cursor.fetchone()

                if user:
                    session['email'] = email
                    return redirect(url_for("homepage.index"))

    return render_template('login.html', title='Login', error='Invalid credentials')

@loginpage.route('/logout')
def logout():
    print("logout triggered")
    # Clear the 'email' key from the session
    session.pop('email', None)
    # Redirect to the login page or any other desired destination
    print("session:", session)
    return redirect(url_for('login.login'))