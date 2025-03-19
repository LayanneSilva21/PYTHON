#Faça um programa que calcule o valor de uma prestação em atraso. Para isso, o programa deve ler o valor da prestação vencida, a taxa periódica de juros
# e o período de atraso. Ao final, o programa deve imprimir o valor da prestação atrasada, o período de atraso, os juros que serão cobrados pelo período de atraso,
# o valor da prestação acrescido dos juros. Considere juros simples.  formula  J = C ∙ i ∙ t

vlpr = float(input('Informe o valor da prestação: '))

t = int(input('Informe o periodo de atraso: '))

i = float(input('Informe a taxa de juros: '))

j = (vlpr * ( i / 100 )) * ( t / 30) 

nv = vlpr + j

print(f'O valor da prestação é {vlpr} \n com juros fica {nv} \n referente ao periodo de {t} e uma taxa de {i}') 

#Faça um programa que leia dois valores inteiros e efetue a adição. Caso o valor somado seja maior que 20, este deverá ser apresentado somando-se a ele mais 8, 
# caso o valor somado seja menor ou igual a 20, este deverá ser apresentado subtraindo-se 5.

n1 = int(input('Digite um valor: '))

n2 = int (input('Digite outro valor: '))

s= n1 + n2

if(s > 20):
    s += 8
else:
    s -= 5

print(f'O valor informado é {s}')

#Faça um programa que leia um número e imprima uma das duas mensagens: "É múltiplo de 3"ou "Não é múltiplo de 3"

n3 = int(input('Informe um valor: '))

if((n3 % 3 ) == 0):
    print(f'O numero é multiplo de 3 ')
else: 
    print(f'Não é multiplo de 3 ')

# Faça um programa que leia um número e informe se ele é ou não divisível por 5.

n4 = int(input('Digite um numero: '))

if((n4 % 5) ==0):
    print(f'O numero é multiplo de 5 ')
else:
    print('O numero não é multiplo de 5 ')

#Faça um programa em C que leia um número e informe se ele é divisível por 3 e por 7.

n5 = int(input('Digite um numero: '))

if((n5 % 3) == 0) + ((n5 % 7) ==0):
    print(f'O numero é multiplo de 3 e 7 ')
else:
    print(f'O numero não é multiplo de 3 e 7 ')

 


