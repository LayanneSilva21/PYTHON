from flask import Flask, request, redirect, render_template, Response, json, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_user, logout_user, current_user
from functools import wraps
from flask_bootstrap import Bootstrap

from config import app_active, app_config

db = SQLAlchemy()  # Inicializa o SQLAlchemy *fora* da função create_app

def create_app(config_name):
    app = Flask(__name__, template_folder='templates')

    app.config.from_object(app_config[config_name])
    # app.config.from_pyfile('config.py') # Já está sendo carregado por from_object
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config['SQLALCHEMY_DATABASE_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['FLASK_ADMIN_SWATCH'] = 'paper'

 

if __name__ == '__main__':
    config_name = app_active or 'development'
    app = create_app(config_name)
    app.run(host='0.0.0.0', port=app.config['PORT_HOST'])

