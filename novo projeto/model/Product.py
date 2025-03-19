from flask_sqlalchemy import SQLAlchemy
from config import app_config, app_active
from model.User import User
from model.Category import Category

config= app_config[app_active]

db=SQLAlchemy(config.APP)

class Product(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80), unique= True, nullable=False)
    description=db.Column(db.Text(), nullable=False)
    qtd=db.Column(db.Integer, niullable=True, default=0)
    image=db.Column(db.Text(), nullable=False)
    price=db.Colmun(db.Numeric(10,2), nullable=False)

date_created= db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)

last_update=db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
     status=db.Column(db.Boolean(), default=1, nullable= True)
     user_created=db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
     category=db.Column(db.Integer, db.ForeignKey(Category.id), nullable=False)


