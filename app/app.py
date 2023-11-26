from flask import Flask, render_template
import pymysql

app = Flask(__name__)

def get_db():
    return pymysql.connect(host='mysql01.cs.virginia.edu',
                           user='nrt3xs',
                           password='UVa107CS4750!',
                           database='nrt3xs',
                           cursorclass=pymysql.cursors.DictCursor)

@app.route('/')
def display_address():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM Addresses"
    cursor.execute(query)
    addresses = cursor.fetchall()
    db.close()
    #this key is the context variable for addresses.html (can have more than one)
    return render_template('addresses.html', addresses=addresses) 

@app.route('/second_page')
def second_page():
    return render_template('second_page.html')

if __name__ == '__main__':
    app.run(debug=True)
