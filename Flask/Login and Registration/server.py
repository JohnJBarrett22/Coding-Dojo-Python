from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "admin"

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/register', methods=['POST'])
def register():

    if len(request.form['first_name']) < 3:
        flash("First Name cannot be blank!", 'first_name')
    elif request.form['first_name'].isalpha() == False:
        flash("First Name cannot have a number in it!", 'first_name')

    if len(request.form['last_name']) < 3:
        flash("Last Name cannot be blank!", 'last_name')
    elif request.form['last_name'].isalpha() == False:
        flash("Last Name cannot have a number in it!", 'last_name')

    mysql = connectToMySQL('login_and_registration')
    query = "SELECT * FROM users WHERE email = %(mail)s"
    data = {
        "mail" : request.form['email']
    }
    users = mysql.query_db(query, data)
    if len(users) == 1:
        flash('E-mail already registered!', 'duplicate')
        return redirect('/')
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!", 'email')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Email must be a valid address!", 'email')

    if len(request.form['password']) < 1:
        flash("Password cannot be blank!", 'password')
    elif len(request.form['password']) < 8:
        flash("Password must be at least 8 characters long!", 'password')

    if len(request.form['confirm_password']) < 1:
        flash("Confirm Password cannot be blank!", 'confirm_password')
    elif len(request.form['confirm_password']) < 8:
        flash("Confirm Password must be at least 8 characters long!", 'confirm_password')
    elif request.form['confirm_password'] != request.form['password']:
        flash('Passwords must match!', 'confirm_password')

    if '_flashes' in session.keys():
        return redirect("/")
    else:
        flash('Thanks for registering your information.', 'success')
        mysql = connectToMySQL('login_and_registration')
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(mail)s, %(psswrd)s, now(), now());"
        hashed_pw = bcrypt.generate_password_hash(request.form['password'])
        data = {
            "fname" : request.form['first_name'],
            "lname" : request.form['last_name'],
            "mail" : request.form['email'],
            "psswrd" : hashed_pw
        }
        mysql.query_db(query, data)
        return redirect("/")


@app.route('/login', methods=['POST'])
def login():

    mysql = connectToMySQL('login_and_registration')
    query = "SELECT * FROM users WHERE email = %(mail)s"
    data = {
        "mail" : request.form['email']
    }
    users = mysql.query_db(query, data)
    if len(users) == 0:
        flash('Invalid credentials!', 'nologin')
        return redirect('/')
    user = users[0]
    session['first_name'] = user['first_name']
    bcrypt.check_password_hash(user['password'], request.form['password'])
    return redirect('/success')


@app.route('/success')
def success():
    hello = session['first_name']
    return render_template("success.html", hello = hello)


@app.route('/signout')
def signout():
    session.clear()
    return redirect('/')


def debugHelp(message = ""):
    print("\n\n-----------------------", message, "--------------------")
    print('REQUEST.FORM:', request.form)
    print('SESSION:', session)

if __name__=="__main__":
    app.run(debug=True)