import os
import random, string 

class Config(object): #caixa de regras de configurações
    CSRF_ENABLED = True #cadeado de segurança contra ataques maliciosos, o True é para ativar
    SECRET = 'Laiane' #é a chave do cadeado
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    #Mostra onde estão os arquivos de layout(HTML)
    ROOT_PATH = os.path.dirname(os.path.abspath(__file__)) #Mostra onde o programa está instalado no computador.
    APP = None #é uma "caixa vazia" que vai guardar o programa principal mais tarde

class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = 'http://localhost:8000'

class TestingConfig(Config):
    #Esse código está configurando um programa para rodar no computador, em modo de teste e depuração, 
    #e vai usar o endereço http://localhost:8000/ para funcionar. É como preparar uma casinha para o programa morar e trabalhar!
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 5000
    URL_MAIN = 'http://localhost:5000' 

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    IP_HOST = 'localhost'
    PORT_HOST = 8080
    URL_MAIN = 'http://localhost:8080'

app_config = {
    'development': DevelopmentConfig(),
    'testing': TestingConfig(),
    'production': ProductionConfig()
}
app_active = os.getenv('FLASK_ENV')
#Esse comando é como perguntar ao computador:"Em qual modo estamos trabalhando?" 
#e guardar a resposta para usar depois. É uma maneira de deixar o programa mais esperto e adaptável! 

 

