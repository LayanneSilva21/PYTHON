from flask_sqlalchemy import SQLAlchemy
from config import app_config, app_active
from model.Role import Role

config = app_config[app_active]

db = SQLAlchemy(config.APP)

class User(db.Model):
    id = db.Column(db.Interger, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable = False)
    email = db.Column(db.String(120), unique=True, nullable = False)
    password = db.Column(db.String(120), nullable = False)

date_created = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable= False)

last_update = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable= True)
   recovery_code=db.Column(db.String(120), nullable= True)
   active=db.Column(db.Boolean, nullable=False)
   role=db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
   