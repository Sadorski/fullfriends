from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'fullfriends')
@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")
    print friends
    for i in range(len(friends)):
        print friends[i]['first_name'], friends[i]['last_name']
    return render_template('index.html', all_friends=friends)

@app.route('/addfriend', methods=['POST'])
def add():
    query = "INSERT INTO friends (first_name, last_name, age, created_at,updated_at) VALUES(:first_name, :last_name, :age, NOW(), NOW())"
    data = {
        'first_name': request.form['name'],
        'last_name': "hello",
        'age': request.form['age'],
    }
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
