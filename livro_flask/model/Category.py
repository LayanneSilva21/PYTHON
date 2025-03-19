from flask_sqlalchemy import SQLAlchemy
from config import app_config, app_active

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False)
    description = db.Column(db.Text(), nullable=False)

    def __repr__(self): # Adiciona o método __repr__ para melhor visualização
        return f"<Category {self.name}>"

    # Outras opções (comentadas, adicione se precisar):
    # products = db.relationship('Product', backref='category')  # Se Category tem relação com Product

    # Exemplo de como criar as tabelas (isso deve ser feito em outro lugar, geralmente em um arquivo separado)
    # with config.APP.app_context(): # Isso é importante para o Flask
    #     db.create_all()