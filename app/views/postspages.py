# postspages.py
from flask import Blueprint, render_template, session
from jinja2 import TemplateNotFound

postspages = Blueprint('postspages', __name__, template_folder='templates')

# @postspages.route("/post/create")
# def create():
#     # Render the create.html template
#     return render_template("create.html", title='Create')


# @postspages.route('/post/<int:id>')
# def post(id):
#     # render the post template with the given id
#     return render_template('post.html', title='Post', id=id)

def get_db():
    return pymysql.connect(
        host='mysql01.cs.virginia.edu',
        user='nrt3xs',
        password='UVa107CS4750!',
        database='nrt3xs',
        cursorclass=pymysql.cursors.DictCursor
    )

@postspages.route('/post/create')
def create():
    if 'email' in session:
        # print("user logged in")
        # print("session:", session)
        # logged_in_user = session['email']
        first_name = session['first_name']
        return render_template('create.html', title='Create', username=first_name)
    else:
        # print("no user logged in")
        return render_template('index.html', title='Home')


@postspages.route('/post')
def post():
    if 'email' in session:
        # print("user logged in")
        # print("session:", session)
        # logged_in_user = session['email']
        first_name = session['first_name']
        return render_template('post.html', title='Post', username=first_name)
    else:
        # print("no user logged in")
        return render_template('index.html', title='Home')
