from flask_sqlalchemy import SQLAlchemy
from config import app_config, app_active
from model.Role import Role  # Certifique-se que Role está definido corretamente

config = app_config[app_active]
db = SQLAlchemy(config.APP)  # Inicialize o SQLAlchemy *depois* de config

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    date_created = db.Column(db.DateTime(6), default=db.func.current_timestamp(), nullable=False)
    last_update = db.Column(db.DateTime(6), onupdate=db.func.current_timestamp(), nullable=True)
    recovery_code = db.Column(db.String(200), nullable=True)
    active = db.Column(db.Boolean(), default=True, nullable=True)  # Correção aqui: True em vez de 1
    role_id = db.Column(db.Integer, db.ForeignKey(Role.id), nullable=False) # Nome da coluna corrigido

    # Adicione um relacionamento para acessar o objeto Role diretamente
    role = db.relationship('Role', backref='users') # Adiciona o relacionamento

    def __repr__(self): # Adiciona o método __repr__ para melhor visualização
        return f"<User {self.username}>"


# Exemplo de como criar as tabelas (isso deve ser feito em outro lugar, geralmente em um arquivo separado)
# with config.APP.app_context(): # Isso é importante para o Flask
#     db.create_all()