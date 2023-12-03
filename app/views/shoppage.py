# searchpages.py
from flask import Blueprint, render_template, request, session, jsonify
from jinja2 import TemplateNotFound
import pymysql

shoppage = Blueprint('shop', __name__, template_folder='templates')


def get_db():
    return pymysql.connect(
        host='mysql01.cs.virginia.edu',
        user='nrt3xs',
        password='UVa107CS4750!',
        database='nrt3xs',
        cursorclass=pymysql.cursors.DictCursor
    )

@shoppage.route("/shop", methods=["GET", "POST"])
def shop():
    if 'email' in session:
        first_name = session['first_name']
        session_user = session['user']

        if request.method == 'POST':
            try:
                selected_filters = request.form.getlist("filters")

                if selected_filters:
                    updated_filters = [f"'{filter}'" for filter in selected_filters]
                    where_clause = f"animal_class IN ({', '.join(updated_filters)})"

                    query = f"SELECT pet_id, breed, name, price, age FROM Pets NATURAL JOIN Breeds NATURAL JOIN Birthdays WHERE {where_clause};"
                else:
                    query = "SELECT pet_id, breed, name, price, age FROM Pets NATURAL JOIN Breeds NATURAL JOIN Birthdays;"

                with get_db() as connection:
                    with connection.cursor() as cursor:
                        cursor.execute(query)
                        filtered_posts = cursor.fetchall()

                return render_template('shop.html', title='Shop', username=first_name, posts=filtered_posts)

            except Exception as e:
                print(e)
                return render_template('error.html', error_message="An error occurred during filtering.")

        else:
            with get_db() as connection:
                with connection.cursor() as cursor:
                    query = "SELECT pet_id, breed, name, price, age FROM Pets NATURAL JOIN Breeds NATURAL JOIN Birthdays;"
                    cursor.execute(query)
                    posts = cursor.fetchall()

            return render_template('shop.html', title='Shop', username=first_name, posts=posts)
    else:
        return render_template('index.html', title='Home')

    