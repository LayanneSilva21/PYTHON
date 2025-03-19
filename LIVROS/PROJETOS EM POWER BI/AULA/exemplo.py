import tkinter as tk
from tkinter import messagebox

def start_game():
    """
    Inicia o jogo quando o usu rio escolhe 'sim' para jogar. Se o
    usu rio digitar qualquer outra entrada, o aplicativo ser  encerrado. Se 'sim'
    for digitado, uma caixa de mensagem aparecer  confirmando o in cio do
    jogo, e a primeira pergunta ser  feita.
    """
    if entry.get().lower() != 'sim':
        root.quit()
    else:
        messagebox.showinfo("Jogo", "Ok! Vamos jogar!")
        ask_question()

def ask_question():
    """
    Pergunta ao usuário qual a resposta para a pergunta. Se a resposta
    for correta, incrementa a pontuação do usuário. Se a resposta for
    incorreta, uma caixa de mensagem aparecerá informando que o usuário
    errou e que ele precisa tentar novamente. Em ambos os casos, a entrada
    do usuário é limpa para que uma nova pergunta possa ser feita.
    """
    answer = entry.get()
    if answer == '5':
        messagebox.showinfo("Resposta", "Você acertou!")
        global score
        score += 1
    else:
        messagebox.showinfo("Resposta", "Você errou! Tente novamente.")
        entry.delete(0, tk.END)

root = tk.Tk()
root.title("Jogo de Perguntas")
root.geometry("300x200")

score = 0

label = tk.Label(root, text="Bem Vindo ao Jogo!")
label.pack()

entry = tk.Entry(root)
entry.pack()

button_start = tk.Button(root, text="Deseja jogar?", command=start_game)
button_start.pack()

label_question = tk.Label(root, text="Quanto   2 + 3?")
label_question.pack()

button_answer = tk.Button(root, text="Responder", command=ask_question)
button_answer.pack()

root.mainloop()





   
