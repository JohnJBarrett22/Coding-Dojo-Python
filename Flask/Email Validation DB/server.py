from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = "admin"

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():

    if len(request.form['email']) < 1:
        flash("Email cannot be blank!", 'email')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Email must be a valid address!", 'email')

    session['email'] = request.form['email']

    if '_flashes' in session.keys():
        return redirect("/")
    else:
        mysql = connectToMySQL('email_validations_db')
        query = "INSERT INTO users (email, created_at) VALUES (%(email)s, now());"
        data = {
            "email" : request.form['email'],
        }
        mysql.query_db(query, data)

        print(query)
        return redirect("/success")

@app.route('/success')
def success():

    mysql = connectToMySQL('email_validations_db')
    print("All Emails...", mysql.query_db("SELECT idusers, email, DATE_FORMAT(created_at, %m/%d/%Y   %I:%i%p) AS time FROM users;"))
    #No quotes query_db other than the ones that surround the select statement.
    mysql = connectToMySQL('email_validations_db')
    users = mysql.query_db("SELECT idusers, email, DATE_FORMAT(created_at, '%m/%d/%Y   %I:%i%p') AS time FROM users;")
    #make sure quotes rotate in the statement or errors.
    print(session)

    return render_template('success.html', users = users)

@app.route('/delete/<userid>')
def delete(userid):
    mysql = connectToMySQL('email_validations_db')
    query = "DELETE FROM users WHERE idusers = %(boom)s;"
    data = {
        "boom" : userid,
    }
    mysql.query_db(query, data)
    return redirect("/success")

if __name__=="__main__":
    app.run(debug=True)