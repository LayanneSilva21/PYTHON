from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from forms import PersonForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///people.db'
db = SQLAlchemy(app)

from models_person import Person

@app.route('/')
def index():
    people = Person.query.all()
    return render_template('index.html', people=people)

@app.route('/add', methods=['GET', 'POST'])
def add_person():
    form = PersonForm()
    if form.validate_on_submit():
        person = Person(name=form.name.data, email=form.email.data)
        db.session.add(person)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_person.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)



