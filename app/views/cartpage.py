# cartpage.py
from flask import Blueprint, render_template, session, request
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




@cartpage.route('/cart', methods=["GET", "POST"])
def cart():
    if 'email' in session:

        if request.method == 'POST':
            try:
                print("in try block")
                first_name = session['first_name']
                logged_in_user = session['email']
                id = request.args.get('petId')
                print("id:", id)
                with get_db() as connection:
                    with connection.cursor() as cursor:
                        query = "SELECT * FROM Purchases WHERE pet_id=%s AND email=%s;"
                        cursor.execute(query,(id,logged_in_user,))
                        item = cursor.fetchone()
                        if not item:
                            query = "INSERT INTO Purchases (pet_id, email) VALUES (%s, %s);"
                            cursor.execute(query,(id,logged_in_user,))
                            connection.commit()
                        query = "DELETE FROM Posts WHERE pet_id = %s;"
                        cursor.execute(query,(id,))
                        connection.commit()
                        print('hekki')
                # with get_db() as connection:
                #     with connection.cursor() as cursor:
                #         query = "SELECT SUM(CONVERT(SUBSTRING(price, 2), DECIMAL(10, 2))) AS total FROM Purchases NATURAL JOIN Pets WHERE email=%s;"
                #         cursor.execute(query,(logged_in_user,))
                #         total = cursor.fetchone()
                #         print("totaljjjjj", total)
                #         return render_template('cart.html', title='Shopping Cart', username=first_name, posts=posts, total=total)

            except Exception as e:
                print(e)

            #     return render_template('cart.html', error_message="An error occurred adding pet to cart.")
        
        # print("user logged in")
        # print("session:", session)
        logged_in_user = session['email']
        first_name = session['first_name']

        with get_db() as connection:
                with connection.cursor() as cursor:
                    # query = "SELECT * FROM Pets NATURAL JOIN Breeds NATURAL JOIN Birthdays NATURAL JOIN Reptiles NATURAL JOIN Water NATURAL JOIN Fish NATURAL JOIN Mammals NATURAL JOIN Birds WHERE pet_id = %s;"
                    # query = "SELECT * FROM Pets NATURAL JOIN Breeds NATURAL JOIN Birthdays WHERE pet_id = %s;"
                    query = "SELECT * FROM Pets NATURAL JOIN Purchases NATURAL JOIN Birthdays WHERE email=%s;"
                    cursor.execute(query,(logged_in_user,))
                    posts = cursor.fetchall() 
                    query = "SELECT SUM(CONVERT(SUBSTRING(price, 2), DECIMAL(10, 2))) AS total FROM Purchases NATURAL JOIN Pets WHERE email=%s;"
                    cursor.execute(query,(logged_in_user,))
                    total = cursor.fetchone()
                    print("totaljjjjj", total)
                    # return render_template('cart.html', title='Shopping Cart', username=first_name, posts=posts, total=total)

        if total['total'] == None:
            total['total'] = 0.00
        return render_template('cart.html', title='Shopping Cart', username=first_name, posts=posts, total=total['total'])
    else:
        # print("no user logged in")
        return render_template('index.html', title='Home')


# @cartpage.route('/cart')
# def cart():
#     # render the shopping cart template
#     return render_template('cart.html', title='Shopping Cart')