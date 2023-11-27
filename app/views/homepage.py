# homepage.py
from flask import Blueprint, render_template
from jinja2 import TemplateNotFound

homepage = Blueprint('homepage', __name__, template_folder='templates')

# A list of posts to display on the home page
posts = [
    {
        "title": "Hello, Flask!",
        "content": "This is my first post using Flask and Jinja."
    },
    {
        "title": "Flask is awesome",
        "content": "I'm learning how to use Flask to create web applications."
    },
    {
        "title": "Flask templates",
        "content": "Flask templates are easy to use and powerful."
    }
]

@homepage.route('/')
def index():
    # Render the index.html template with the posts variable
    return render_template("index.html", title='Home', posts=posts)