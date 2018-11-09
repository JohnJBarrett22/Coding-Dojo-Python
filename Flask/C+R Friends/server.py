from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL
app = Flask(__name__)

@app.route('/')
def index():
    mysql = connectToMySQL('cr_friends')
    print("All my friends...", mysql.query_db("SELECT * FROM friends;"))
    mysql = connectToMySQL('cr_friends')
    friends = mysql.query_db("SELECT * FROM friends;")
    return render_template('index.html', friends = friends)

@app.route('/add', methods=['POST'])
def add():
    mysql = connectToMySQL('cr_friends')
    query = ("INSERT INTO friends (first_name, last_name, occupation) VALUES (%(first_name)s, %(last_name)s, %(occupation)s);")
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "occupation" : request.form['occupation']
    }
    mysql.query_db(query, data)
    
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
