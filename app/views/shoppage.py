# searchpages.py
from flask import Blueprint, render_template, request, session
from jinja2 import TemplateNotFound
import pymysql

shoppage = Blueprint('shop', __name__, template_folder='templates')

# A list of users to display on the search results page
# users = [
#     {
#         "username": "alice",
#         "bio": "I love Flask and Python."
#     },
#     {
#         "username": "bob",
#         "bio": "I'm a beginner in web development."
#     },
#     {
#         "username": "charlie",
#         "bio": "I'm a fan of open source software."
#     }
# ]

# @shop.route("/shop", methods=["GET", "POST"])
# def search():
#     # If the request method is POST, get the query and filter the users list
#     if request.method == "POST":
#         query = request.form.get("query")
#         # You can use your own logic to search for users here
#         results = [user for user in users if query.lower() in user["username"].lower()]
#         # Render the results.html template with the query and results variables
#         return render_template("results.html", query=query, results=results)
#     # If the request method is GET, render the search.html template
#     return render_template("shop.html", title='Shop')

# @shoppage.route("/shop", methods=["GET", "POST"])
# def shop():
#     # Render the index.html template with the posts variable
#     return render_template("shop.html", title='Shop', posts=posts)


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
        # print("user logged in")
        # print("session:", session)
        # logged_in_user = session['email']
        first_name = session['first_name']
        session_user = session['user']
        with get_db() as connection:
                    with connection.cursor() as cursor:
                        query = "SELECT pet_id, breed, name, price, age FROM Pets NATURAL JOIN Breeds NATURAL JOIN Birthdays;"
                        cursor.execute(query)
                        posts = cursor.fetchall()
        return render_template('shop.html', title='Shop', username=first_name, posts=posts)
    else:
        # print("no user logged in")
        return render_template('index.html', title='Home')