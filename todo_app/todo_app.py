from flask import Flask , render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os


app = Flask(__name__)
app.config['SEKRET_KEY'] = ''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION']  = False 

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.column(db.Integer, primary_key = True)
    content = db.column(db.string(200), nullable = False)
    date_created = db.column(db.DateTime, default = datetime.now())

    def __repr__(self):
        return f"<Task {self.id}>"

with app.app_contex():
    db.create_all()

@app.route('/', methods = ['GET'])
def index():
    tasks = Task.query.ordr_by(Task.date_created.desk()).all()  #filter для фильтрации all для вывода всего
    return render_template('index.html', tasks = tasks)

@app.route('/add', methods = ['POST'])
def add_task():
    task_kontent = request.from('content')
    if not task_kontent:
        flash('pusto ne mozhet','error')
        return redirect(url_for('index'))
    
    new_task = Task(content = task_kontent)
    try:
        db.session.add(new_task)
        db.session.commit()
        flash("Saved", "success")
    except Exeption as e:
        db.session.rollback()
        flash("exeption!!!","error")
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_task(id):
    task = Task.query.get_or_404(id)
     try:
        db.session.delete(new_task)
        db.session.commit()
        flash("Delete", "success")
    except Exeption as e:
        db.session.rollback()
        flash("exeption from delit!!!","error")
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug = True)

