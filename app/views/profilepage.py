# profilepage.py
from flask import Blueprint, render_template, session, request, redirect, url_for
from jinja2 import TemplateNotFound
import pymysql, bcrypt

profilepage = Blueprint('profilepage', __name__, template_folder='templates')

# # @profilepage.route("/profile/<username>")
# @profilepage.route("/profile")
# # def profile(username):
# def profile():
#     # Render the profile.html template with the username variable
#     # return render_template("profile.html", title='Profile', username=username)
#     return render_template("profile.html", title='Profile')

def get_db():
    return pymysql.connect(
        host='mysql01.cs.virginia.edu',
        user='nrt3xs',
        password='UVa107CS4750!',
        database='nrt3xs',
        cursorclass=pymysql.cursors.DictCursor
    )

@profilepage.route('/profile', methods=['GET', 'POST'])
@profilepage.route('/update_password', methods=['POST'])
def profile():
    try:
        if 'user' in session:
            # print("user logged in")
            # print("session:", session)
            logged_in_user = session['email']
            first_name = session['first_name']
            session_user = session['user']
            
            #password update
            if request.method == 'POST':
                # Handle password update logic
                current_password = request.form.get("password")
                new_password = request.form.get("new_password")
                confirm_new_password = request.form.get("confirm_new_password")


                if new_password == current_password and (bcrypt.checkpw(current_password.encode('utf-8'), session_user['password'].encode('utf-8'))):
                    return render_template('profile.html', title='Profile', password_error='New Password Cannot be Current Password.', username=first_name, user=session_user)

                if new_password != confirm_new_password:
                    return render_template('profile.html', title='Profile', password_error='Password Update Failed.', username=first_name, user=session_user)

                new_hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())

                with get_db() as connection:
                    with connection.cursor() as cursor:
                        # paramertized queries
                        query = "SELECT * FROM Users WHERE email=%s AND first_name=%s"
                        cursor.execute(query, (logged_in_user,first_name,))
                        user = cursor.fetchone()

                        if user and (bcrypt.checkpw(current_password.encode('utf-8'), user['password'].encode('utf-8'))):
                            # paramertized queries
                            query = "UPDATE Users SET password=%s WHERE email=%s AND first_name=%s"
                            cursor.execute(query, (new_hashed_password, logged_in_user,first_name,))
                            connection.commit()
                            return render_template('profile.html', title='Profile', password_error='Password Update Successful!', username=first_name, user=user)
                        else:
                            return render_template('profile.html', title='Profile', password_error='Password Update Failed.', username=first_name, user=user)
            #no password update
            else:
                with get_db() as connection:
                    with connection.cursor() as cursor:
                        # paramertized queries
                        query = "SELECT * FROM Users WHERE email=%s AND first_name=%s"
                        cursor.execute(query, (logged_in_user,first_name,))
                        user = cursor.fetchone()

                return render_template('profile.html', title='Profile', username=first_name, user=user)

        else:
            return render_template('index.html', title='Home')
    except Exception as e:
        print(e)
        return render_template('profile.html', title='Profile', error='Whoops... something happened. Please login again.')
            
@profilepage.route('/grant_admin_privileges', methods=['POST'])
def grant_admin_privileges():
    try:
        logged_in_user = session['email']
        first_name = session['first_name']
        session_user = session['user']
        if 'email' in session and request.method == 'POST':
            # print("in here")

            admin_password = "admin_password"  # Replace with your actual admin password
            user_admin_password = request.form.get("admin")
            admin_to_computing_id = request.form.get("computing_id")

            if admin_password == user_admin_password:
                # print("written correctly")
                with get_db() as connection:
                    with connection.cursor() as cursor:
                        # Modify the query to grant the necessary privileges
                        # print("at query statement")
                        #grant privledges to one of the sub accounts in my database since we are on the cs server we cant really do much with it
                        query = f"GRANT ALL PRIVILEGES ON nrt3xs TO '{admin_to_computing_id}'@'%';"
                        cursor.execute(query)
                        connection.commit()
                # print("before return")
                # return redirect(url_for('profilepage.profile', title='Profile', admin_error='Admin Access Granted.', username=first_name, user=session_user))
                print(session)
                print(session_user)
                return render_template('profile.html', title='Profile', admin_error='Admin Access Granted.', username=first_name, user=session_user)

            else:
                # return redirect(url_for('profilepage.profile', title='Profile', admin_error='Incorrect admin password.', username=first_name, user=session_user))
                return render_template('profile.html', title='Profile', admin_error='Incorrect admin password.', username=first_name, user=session_user)

    except Exception as e:
        print(e)
        return render_template('profile.html', title='Profile', error='Whoops... something happened. Please try again.', username=first_name)