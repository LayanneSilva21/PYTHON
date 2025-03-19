from flask_sqlalchemy import SQLAlchemy
from config import app_config, app_active
from model.User import User
from model.Category import Category

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.Text(), nullable=False)
    qtd = db.Column(db.Integer, nullable=True, default=0)
    image = db.Column(db.Text(), nullable=True)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    date_created = db.Column(db.DateTime(6), default=db.func.current_timestamp(), nullable=False)
    last_update = db.Column(db.DateTime(6), onupdate=db.func.current_timestamp(), nullable=False)
    status = db.Column(db.Boolean(), default=True, nullable=True)  # True em vez de 1
    user_created_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)  # user_created_id para chave estrangeira
    category_id = db.Column(db.Integer, db.ForeignKey(Category.id), nullable=False)  # category_id para chave estrangeira

    # Adicione relacionamentos para acessar User e Category diretamente:
    user_created = db.relationship('User', backref='products_created')  # backref para acessar os produtos criados por um usuário
    category = db.relationship('Category', backref='products')  # backref para acessar os produtos de uma categoria

    def __repr__(self):
        return f"<Product {self.name}>"

# Exemplo de como criar as tabelas (isso deve ser feito em outro lugar, geralmente em um arquivo separado)
# with config.APP.app_context():  # Isso é importante para o Flask
#     db.create_all()