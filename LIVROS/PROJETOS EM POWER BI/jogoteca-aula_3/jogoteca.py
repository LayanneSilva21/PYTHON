from flask import Flask, render_template, request, redirect, session, flash, url_for

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome  # Name of the game
        self.categoria = categoria  # Category of the game
        self.console = console  # Console of the game

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Hack n Slash', 'PS2')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
lista = [jogo1, jogo2, jogo3,]

class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha

usuario1 = Usuario("Laiane Silva", "LS", "python")
usuario2 = Usuario("Camila Ferreira", "Mila", "paozinho")
usuario3 = Usuario("Guilherme Louro", "Cake", "python_eh_vida")

usuarios = { usuario1.nickname : usuario1,
             usuario2.nickname : usuario2,
             usuario3.nickname : usuario3 }

app = Flask(__name__)
app.secret_key = 'Laiane'

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
   
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    # If the user is logged in, render the new game page.
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form.get('nome')
    categoria = request.form.get('categoria')
    console = request.form.get('console')
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST', 'GET'])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario=usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname 
            flash(usuario.nickname + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect('/{}'.format(proxima_pagina))
        else:
            flash('Usuario não logado!')
            return redirect(url_for('login'))

@app.route('/logout')
def logout():
    
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('login'))

app.run(debug=True)