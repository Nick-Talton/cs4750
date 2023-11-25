from flask import Flask, render_template
import pymysql

app = Flask(__name__)


db = pymysql.connect(host='mysql01.cs.virginia.edu',
                     user='nrt3xs',
                     password='UVa107CS4750!',
                     database='nrt3xs',
                     cursorclass=pymysql.cursors.DictCursor)

# Create a cursor to interact with the database
cursor = db.cursor()

@app.route('/')
def display_accounts():
    query = "SELECT * FROM account"
    cursor.execute(query)
    accounts = cursor.fetchall()

    #db.close()

    return render_template('accounts.html', accounts=accounts)

if __name__ == '__main__':
    app.run(debug=True)
