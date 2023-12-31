# loginpage.py
from flask import Blueprint, render_template, request, redirect, url_for, session
import pymysql
import bcrypt

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
                # paramertized queries
                query = "SELECT * FROM Users WHERE email=%s"
                cursor.execute(query, (email,))
                user = cursor.fetchone()
                #all the users are going to fail passwordcheck now unless we hash them all so just make a user account for modifying
                if user and (bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8'))):
                    session['email'] = email
                    session['first_name'] = user['first_name']
                    session['user'] = user
                    #print(session)
                    return redirect(url_for("homepage.index"))
                else:
                    return render_template('login.html', title='Login', error='Invalid Credentials')

    if 'error' in request.args:
        error = request.args.get('error')
        return render_template('login.html', title='Login', error=error)
    return render_template('login.html', title='Login')

@loginpage.route('/logout')
def logout():
    # print("logout triggered")
    # Clear the 'email' key from the session
    session.pop('email', None)
    session.pop('first_name', None)
    session.pop('user', None)
    # Redirect to the login page or any other desired destination
    # print("session:", session)
    return redirect(url_for('login.login'))