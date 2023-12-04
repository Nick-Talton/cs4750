# confirmationpage.py
from flask import Blueprint, render_template, session, request
from jinja2 import TemplateNotFound
from sqlalchemy import text
from datetime import datetime
import pymysql

postconfirmationpage = Blueprint('postconfirmationpage', __name__, template_folder='templates')

def get_db():
    return pymysql.connect(
        host='mysql01.cs.virginia.edu',
        user='nrt3xs',
        password='UVa107CS4750!',
        database='nrt3xs',
        cursorclass=pymysql.cursors.DictCursor
    )

@postconfirmationpage.route('/postconfirmation', methods=['POST'])
def postconfirmation():
    if 'email' in session:
        executeSqlQueries(request, session['email'])

        first_name = session['first_name']
        return render_template('postconfirmation.html', title='Post Confirmation ', username=first_name)
    else:
        return render_template('index.html', title='Home')

def executeSqlQueries(request, email):
    createBreed(request.form)
    createBirthday(request.form)
    pet_id = createPet(request.form)
    if request.form['path'] == "mammal":
        createMammalPost(pet_id, request.form)
    elif request.form['path'] == "fish":
        createFishPost(pet_id, request.form)
    elif request.form['path'] == "reptile":
        createReptilePost(pet_id, request.form)
    elif request.form['path'] == "bird":
        createBirdPost(pet_id, request.form)
    createPost(pet_id, request.form, email)

def createBirthday(requestObject):
    birth_date = requestObject['dob']
    birth_date = datetime.strptime(birth_date, '%Y-%m-%d').date()
    today = datetime.today().date()

    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    with get_db() as connection:
        with connection.cursor() as cursor:
            # paramertized queries
            query = "INSERT INTO Birthdays (birthday, age) VALUES (%s, %s)"
            cursor.execute(query, (
                birth_date,
                age,))
            connection.commit()

def createBreed(requestObject):
    with get_db() as connection:
        with connection.cursor() as cursor:
            # paramertized queries
            query = "INSERT INTO Breeds (breed, animal_class) VALUES (%s, %s)"
            cursor.execute(query, (
                requestObject['breed'],
                requestObject['path'],))
            connection.commit()


def createPet(requestObject):
    pet_id = 0
    with get_db() as connection:
        with connection.cursor() as cursor:
            # paramertized queries
            pet_id = "SELECT MAX(pet_id) FROM Pets"
            cursor.execute(pet_id)
            pet_id = cursor.fetchone()['MAX(pet_id)']
            if pet_id is None: 
                pet_id = 0
            else:
                pet_id = pet_id + 1
                
            query = "INSERT INTO Pets (pet_id, name, price, gender, breed, birthday, color, description, medical_condition, care_level, diet) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (
                pet_id,
                requestObject['name'],
                requestObject['price'],
                requestObject['gender'],
                requestObject['breed'],
                requestObject['dob'],
                requestObject['color'],
                requestObject['description'],
                requestObject['medical_conditions'],
                requestObject['care_level'],
                requestObject['diet']))
            connection.commit()
    return pet_id

def createPost(pet_id, requestObject, email):
    with get_db() as connection:
        with connection.cursor() as cursor:
            # paramertized queries
            query = "INSERT INTO Posts (pet_id, email) VALUES (%s, %s)"
            cursor.execute(query, (
                pet_id,
                email,))
            connection.commit()

def createMammalPost(pet_id, requestObject):
    with get_db() as connection:
        with connection.cursor() as cursor:
            # paramertized queries
            query = "INSERT INTO Mammals (pet_id, eye_color, weight) VALUES (%s, %s, %s)"
            cursor.execute(query, (
                pet_id,
                requestObject['eye_color'],
                requestObject['weight'],))
            connection.commit()

def createFishPost(pet_id, requestObject):
    with get_db() as connection:
        with connection.cursor() as cursor:
            # paramertized queries
            query = "INSERT INTO Fish (pet_id, min_tank_size, water_type, temperament) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (
                pet_id,
                requestObject['min_tank_size'],
                requestObject['water_type'],
                requestObject['temperament'],))
            connection.commit()

def createReptilePost(pet_id, requestObject):
    with get_db() as connection:
        with connection.cursor() as cursor:
            # paramertized queries
            query = "INSERT INTO Reptiles (pet_id, habitat) VALUES (%s, %s)"
            cursor.execute(query, (
                pet_id,
                requestObject['habitat'],))
            connection.commit()

def createBirdPost(pet_id, requestObject):
    with get_db() as connection:
        with connection.cursor() as cursor:
            # paramertized queries
            query = "INSERT INTO Birds (pet_id, wing_span, noise_level) VALUES (%s, %s, %s)"
            cursor.execute(query, (
                pet_id,
                requestObject['wing_span'],
                requestObject['noise_level'],))
            connection.commit()
