#JOGO DA FORCA

import random
from string import ascii_letters

def jogar():
    print('**********************************************')
    print('*******Bem vindo ao Jogo da Forca!************')
    print('**********************************************')

    palavras = ['BANANA', 'PYTHON', 'DANIEL', 'DESENVOLVIMENTO', 'SISTEMA']
    palavra_secreta = random.choice(palavras)

    letras_acertadas = ['_' for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while not enforcou and not acertou:
        chute = input('Qual a letra? ').strip().upper()
        if len(chute) != 1:
            print('Informe apenas uma letra!')
            continue
        if chute not in ascii_letters:
            print('Informe apenas letras!')
            continue

        if chute in palavra_secreta:
            for posicao, letra in enumerate(palavra_secreta):
                if chute == letra:
                    letras_acertadas[posicao] = letra
        else:
            erros += 1

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print('Parabéns, Você Ganhou!!!')
    else:
        print('Que pena, você perdeu!!!')

    print('Fim de Jogo!!!')

# Chama a função para iniciar o jogo
jogar()

