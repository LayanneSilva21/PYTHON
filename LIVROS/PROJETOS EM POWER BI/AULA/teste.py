print('*********************')
print('**Bem vindo ao jogo**')
print('*********************')

print('Quantos discipulos Jesus teve?\n')

while True:
    resposta = input('Digite a resposta: ')

    if resposta.isdigit():
        resposta = int(resposta)
        if resposta == 12:
            print('Voce acertou!')
            break
        else:
            print('Voce errou! Tente novamente.')
    else:
        print('Voce precisa digitar um numero!')

print('Fim do jogo!')
