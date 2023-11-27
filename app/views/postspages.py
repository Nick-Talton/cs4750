# postspages.py
from flask import Blueprint, render_template
from jinja2 import TemplateNotFound

postspages = Blueprint('postspages', __name__, template_folder='templates')

@postspages.route("/post/create")
def create():
    # Render the create.html template
    return render_template("create.html", title='Create')


@postspages.route('/post/<int:id>')
def post(id):
    # render the post template with the given id
    return render_template('post.html', title='Post', id=id)