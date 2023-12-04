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

@profilepage.route('/profile/myposts', methods=['GET', 'POST'])
def myposts():
    try:
        if 'user' in session:
            # print("user logged in")
            # print("session:", session)
            logged_in_user = session['email']
            first_name = session['first_name']
            session_user = session['user']

            with get_db() as connection:
                with connection.cursor() as cursor:
                    # paramertized queries
                    query = "(SELECT pet_id, name, breed, age, price, email, '0' AS sale_finalized FROM Posts NATURAL JOIN Pets NATURAL JOIN Breeds NATURAL JOIN Birthdays WHERE email=%s) UNION (SELECT pet_id, name, breed, age, price, seller as email, sale_finalized FROM Purchases NATURAL JOIN Pets NATURAL JOIN Breeds NATURAL JOIN Birthdays WHERE seller=%s)" 

                    cursor.execute(query, (logged_in_user,logged_in_user))
                    posts = cursor.fetchall()
                
                if not posts:
                    return render_template('myposts.html', title='Profile', post_error='No Posts Found.', username=first_name, user=session_user)

            return render_template('myposts.html', title='Profile', username=first_name, user=session_user, posts=posts)

        else:
            return render_template('index.html', title='Home')
    except Exception as e:
        print(e)
        return render_template('profile.html', title='Profile', error='Whoops... something happened. Please login again.')


@profilepage.route('/profile/myposts/deletepost', methods=['GET', 'POST'])
def deletepost():
    try:
        if 'user' in session:
            # print("user logged in")
            # print("session:", session)
            logged_in_user = session['email']
            first_name = session['first_name']
            session_user = session['user']

            if request.method == 'POST':
                # Handle password update logic
                pet_id = request.args.get('petId')

                print("pet_id:", pet_id)

                with get_db() as connection:
                    with connection.cursor() as cursor:
                        # paramertized queries
                        query = "SELECT * FROM Posts WHERE pet_id=%s AND email=%s;"
                        cursor.execute(query,(pet_id,logged_in_user,))
                        item = cursor.fetchone()
                        print("item:", item)
                        if not item:
                            print("in here")
                            query = "SELECT * FROM Purchases WHERE pet_id=%s AND seller=%s;"
                            cursor.execute(query,(id,logged_in_user,))
                            item2 = cursor.fetchone()
                            print("item2:", item2)
                            if item2:
                                query = "DELETE FROM Purchases WHERE pet_id = %s AND seller=%s;"
                                cursor.execute(query,(id,logged_in_user,))
                                connection.commit()
                                print('hihihi')
                        else:    
                            query = "DELETE FROM Posts WHERE pet_id = %s AND email=%s;"
                            cursor.execute(query,(id,logged_in_user,))
                            connection.commit()
                            print('hekki')

                return redirect(url_for('profilepage.myposts', title='Profile', username=first_name, user=session_user))

            else:
                return render_template('index.html', title='Home')
        else:
            return render_template('index.html', title='Home')
    except Exception as e:
        print(e)
        return render_template('profile.html', title='Profile', error='Whoops... something happened. Please login again.')







@profilepage.route('/profile/orders', methods=['GET', 'POST'])
def orders():
    try:
        if 'user' in session:
            # print("user logged in")
            # print("session:", session)
            logged_in_user = session['email']
            first_name = session['first_name']
            session_user = session['user']

            with get_db() as connection:
                with connection.cursor() as cursor:
                    # paramertized queries
                    query = "SELECT pet_id, name, breed, age, price, seller as email, sale_finalized FROM Purchases NATURAL JOIN Pets NATURAL JOIN Breeds NATURAL JOIN Birthdays WHERE email=%s AND sale_finalized=%s"
                    cursor.execute(query, (logged_in_user,'1'))
                    orders = cursor.fetchall()
            if not orders:
                return render_template('orders.html', title='Profile', order_error='No Orders Found.', username=first_name, user=session_user)

            return render_template('orders.html', title='Profile', username=first_name, user=session_user, orders=orders)

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
            user_type = request.form.get("userType")
            # print("User type: ", user_type)

            user_types = {"Admin" : "ALL PRIVILEGES", "Employee" : "SELECT, UPDATE, ALTER", "User" : "SELECT"}

            if admin_password == user_admin_password:
                # print("written correctly")
                with get_db() as connection:
                    with connection.cursor() as cursor:
                        # Modify the query to grant the necessary privileges
                        # print("at query statement")
                        #grant privledges to one of the sub accounts in my database since we are on the cs server we cant really do much with it
                        query = f"GRANT {user_types[user_type]} ON nrt3xs TO '{admin_to_computing_id}'@'%';"
                        # print(query)
                        cursor.execute(query)
                        connection.commit()
                # print("before return")
                # return redirect(url_for('profilepage.profile', title='Profile', admin_error='Admin Access Granted.', username=first_name, user=session_user))
                # print("session:", session)
                # print("session user:", session_user)
                return render_template('profile.html', title='Profile', admin_error='Admin Access Granted.', username=first_name, user=session_user)

            else:
                # return redirect(url_for('profilepage.profile', title='Profile', admin_error='Incorrect admin password.', username=first_name, user=session_user))
                return render_template('profile.html', title='Profile', admin_error='Incorrect admin password.', username=first_name, user=session_user)

    except Exception as e:
        print(e)
        return render_template('profile.html', title='Profile', error='Whoops... something happened. Please try again.', username=first_name)


@profilepage.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    try:
        logged_in_user = session['email']
        first_name = session['first_name']
        session_user = session['user']
        if 'email' in session and request.method == 'POST':
            del_user_password = request.form.get("del_user_password")
            confirmation = request.form.get("confirmation")
            hashed_password = bcrypt.hashpw(del_user_password.encode('utf-8'), bcrypt.gensalt())

            with get_db() as connection:
                    with connection.cursor() as cursor:
                        # paramertized queries
                        query = "SELECT * FROM Users WHERE email=%s AND first_name=%s"
                        cursor.execute(query, (logged_in_user,first_name,))
                        user = cursor.fetchone()
                        print(user)

                        if user and (bcrypt.checkpw(del_user_password.encode('utf-8'), user['password'].encode('utf-8'))) and confirmation == "CONFIRM":
                            # paramertized queries
                            print("In here")
                            query = "DELETE FROM Users WHERE email=%s"
                            cursor.execute(query, (logged_in_user,))
                            connection.commit()
                            session.pop('email', None)
                            session.pop('first_name', None)
                            session.pop('user', None)
                            return redirect(url_for('login.login', title='Login', error='Account Deleted'))
                        else:
                            print("Failed to delete")
                            return render_template('profile.html', title='Profile', password_error='Account Deletion Failed', username=first_name, user=user)
                        
        return render_template('profile.html', title='Profile', password_error='Account Deletion Failed', username=first_name, user=session_user)


    except Exception as e:
        print(e)
        return render_template('profile.html', title='Profile', error='Whoops... something happened. Please try again.', username=first_name)