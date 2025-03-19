from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import app_active, app_config
from model.Role import Role
from model.User import User
from model.Category import Category
from model.Product import Product

config = app_config[app_active]
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False)

    def __repr__(self):
        return f"<Role {self.name}>"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    date_created = db.Column(db.DateTime(6), default=db.func.current_timestamp(), nullable=False)
    last_update = db.Column(db.DateTime(6), onupdate=db.func.current_timestamp(), nullable=True)
    recovery_code = db.Column(db.String(200), nullable=True)
    active = db.Column(db.Boolean(), default=True, nullable=True)  # True para booleano
    role_id = db.Column(db.Integer, db.ForeignKey(Role.id), nullable=False) # _id na chave estrangeira

    role = db.relationship('Role', backref='users') # relacionamento

    def __repr__(self):
        return f"<User {self.username}>"


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.Text(), nullable=True)

    def __repr__(self):
        return f"<Category {self.name}>"

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.Text(), nullable=False)
    qtd = db.Column(db.Integer, nullable=True, default=0)
    image = db.Column(db.Text(), nullable=True)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    date_created = db.Column(db.DateTime(6), default=db.func.current_timestamp(), nullable=False)
    last_update = db.Column(db.DateTime(6), onupdate=db.func.current_timestamp(), nullable=True)
    status = db.Column(db.Boolean(), default=True, nullable=True)  # True para booleano
    user_created_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False) # _id
    category_id = db.Column(db.Integer, db.ForeignKey(Category.id), nullable=False) # _id

    user_created = db.relationship('User', backref='products_created')
    category = db.relationship('Category', backref='products')


    def __repr__(self):
        return f"<Product {self.name}>"

if __name__ == '__main__':
    manager.run()