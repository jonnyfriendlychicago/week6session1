from app import app
from flask import Flask, render_template, redirect, session, request, flash
import re
# from  flask_bcrypt import Bcrypt
from app.models.user import User
from app.models.toDo import Tasks


@app.route('/toDoApp')
def toDo():
    if 'user_id' not in session:
        flash("You are not authorized to view that")
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    return render_template('toDo.html', user=User.getOne(data), tasks=Tasks.getAll())