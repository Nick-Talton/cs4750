# confirmationpage.py
from flask import Blueprint, render_template, session, request
from jinja2 import TemplateNotFound
import pymysql

confirmationpage = Blueprint('confirmationpage', __name__, template_folder='templates')

# @confirmationpage.route("/confirmation")
# # def profile(username):
# def confirmation():
#     # Render the profile.html template with the username variable
#     # return render_template("profile.html", title='Profile', username=username)
#     return render_template("confirmation.html", title='Confirmation')

def get_db():
    return pymysql.connect(
        host='mysql01.cs.virginia.edu',
        user='nrt3xs',
        password='UVa107CS4750!',
        database='nrt3xs',
        cursorclass=pymysql.cursors.DictCursor
    )

@confirmationpage.route('/confirmation', methods=['GET', 'POST'])
def confirmation():
    if 'email' in session:
        # print("user logged in")
        # print("session:", session)
        # logged_in_user = session['email']
        print('in confirmation')
        if request.method == 'POST':
            print('in post')
            try:
                print("in try block")
                first_name = session['first_name']
                logged_in_user = session['email']
                id = request.args.get('petId')
                with get_db() as connection:
                    with connection.cursor() as cursor:
                        query = "UPDATE Purchases SET sale_finalized = %s WHERE email=%s"
                        cursor.execute(query,('1',logged_in_user,))
                        connection.commit()
                        print('hekki')
            except Exception as e:
                print(e)
        print('out of post')
        first_name = session['first_name']
        return render_template('confirmation.html', title='Confirmation', username=first_name)
    else:
        # print("no user logged in")
        return render_template('index.html', title='Home')
