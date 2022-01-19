from flask_app import app
from flask import Flask, render_template, redirect, session, request, flash
from flask_app.models.user import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/createUser/', methods=['POST'])
def createUser():
    isValid = User.validate(request.form)
    if not isValid:
        return redirect('/')
    data = {
        'username': request.form['username'],
        'userKey': request.form['userKey']
    }
    User.save(data)
    return redirect('/dashboard/')

@app.route('/dashboard/')
def dashboard():
    users = User.getAll()
    return render_template('dashboard.html', users=users)