#EXERCICOS PYTHON 

# Faça um programa que leia um número e indique se o número está compreendido entre 20 e 50 ou não.
def numero():
    num = int(input('Digite um numero: '))
    if num >= 20 and num <=50:
        print('O numero esta entre 20 e 50')
    else:
        print('O numero não esta entre 20 e 50')

numero()

#A confederação brasileira de natação irá promover eliminatórias para o próximo mundial. Faça um programa que receba a idade de um nadador e imprima
#a sua categoria segundo a tabela a seguir:
#Categoria Idade Infantil A 5 - 7 anos | Infantil B 8 - 10 anos | Juvenil A 11 - 13 anos |Juvenil B 14 - 17 anos | Sênior maiores de 18 anos

def idade():
    idade = int(input('Digite sua idade: '))
    if idade <= 7:
        print('Infantil A')
    elif idade <= 10:
        print('Infantil B')
    elif idade <= 13:
        print('Juvenil A')
    elif idade <= 17:
        print('Juvenil B')
    else:
        print('Seniors')

idade()


