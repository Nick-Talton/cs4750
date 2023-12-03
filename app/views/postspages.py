# postspages.py
from flask import Blueprint, render_template, session, request
from jinja2 import TemplateNotFound
import pymysql

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

@postspages.route('/post/create', methods=['GET', 'POST'])
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


@postspages.route('/post/<int:id>',  methods=['GET', 'POST'])
def post(id):
    if 'email' in session:


        # print("user logged in")
        # print("session:", session)
        # logged_in_user = session['email']
        first_name = session['first_name']
        with get_db() as connection:
                with connection.cursor() as cursor:
                    # query = "SELECT * FROM Pets NATURAL JOIN Breeds NATURAL JOIN Birthdays NATURAL JOIN Reptiles NATURAL JOIN Water NATURAL JOIN Fish NATURAL JOIN Mammals NATURAL JOIN Birds WHERE pet_id = %s;"
                    # query = "SELECT * FROM Pets NATURAL JOIN Breeds NATURAL JOIN Birthdays WHERE pet_id = %s;"
                    query = "SELECT * FROM Pets NATURAL JOIN Breeds NATURAL JOIN Birthdays LEFT OUTER JOIN Reptiles ON Pets.pet_id = Reptiles.pet_id LEFT OUTER JOIN Mammals ON Pets.pet_id = Mammals.pet_id LEFT OUTER JOIN Birds ON Pets.pet_id = Birds.pet_id LEFT OUTER JOIN Fish on Pets.pet_id = Fish.pet_id LEFT OUTER JOIN Water ON Fish.water_type = Water.water_type WHERE Pets.pet_id = %s;"
                    cursor.execute(query,(id,))
                    post = cursor.fetchall() 
        p = post[0] if post else None
        return render_template('post.html', title='Post', username=first_name, post=p)
    else:
        # print("no user logged in")
        return render_template('index.html', title='Home')
