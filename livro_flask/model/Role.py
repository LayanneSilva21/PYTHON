from flask_sqlalchemy import SQLAlchemy
from config import app_active, app_config

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False)

    def __repr__(self):  # Adiciona __repr__ para melhor visualização
        return f"<Role {self.name}>"

# Exemplo de como criar as tabelas (isso deve ser feito em outro lugar, geralmente em um arquivo separado)
# with config.APP.app_context(): # Isso é importante para o Flask
#     db.create_all()