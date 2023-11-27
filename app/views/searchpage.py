# searchpages.py
from flask import Blueprint, render_template, request
from jinja2 import TemplateNotFound

searchpage = Blueprint('searchpage', __name__, template_folder='templates')

# A list of users to display on the search results page
users = [
    {
        "username": "alice",
        "bio": "I love Flask and Python."
    },
    {
        "username": "bob",
        "bio": "I'm a beginner in web development."
    },
    {
        "username": "charlie",
        "bio": "I'm a fan of open source software."
    }
]

@searchpage.route("/search", methods=["GET", "POST"])
def search():
    # If the request method is POST, get the query and filter the users list
    if request.method == "POST":
        query = request.form.get("query")
        # You can use your own logic to search for users here
        results = [user for user in users if query.lower() in user["username"].lower()]
        # Render the results.html template with the query and results variables
        return render_template("results.html", query=query, results=results)
    # If the request method is GET, render the search.html template
    return render_template("search.html", title='Search')