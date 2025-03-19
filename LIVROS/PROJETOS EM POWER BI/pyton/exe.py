#Faça um programa que leia o valor de um produto, o percentual do desconto desejado e imprima o valor do desconto e o valor do produto subtraindo o desconto.

vlprd = int(input('Digite o valor do produto: '))
perDc = float(input('Informe o valor de desconto: '))

vlrDesc = vlprd - (vlprd * (perDc / 100 ))

print(f'O valor do produto é {vlprd} e o desconto aplicado será de {perDc}%, valor final {vlrDesc}')

#Faça um programa que calcule o reajuste do salário de um funcionário. Para isso, o programa deverá ler o salário atual do funcionário e ler o percentual de
#reajuste. Ao final imprimir o valor do novo salário.

reaj = int(input('Digite o valor do reajuste: '))

sal = float(input('Digite o valor do salario: '))

perc = sal + (sal * (reaj/ 100))

print(f'O valor do salario era de {sal} e o reajuste será de {reaj}%, o novo salario será no valor de {perc}')

#Faça um programa que calcule a conversão entre graus centígrados e Fahrenheit. Para isso, leia o valor em centígrados e calcule com base na fórmula a seguir. 
# Após calcular o programa deve imprimir o resultado da conversão.

csl = float(input('Informe a temperatura em graus ºC: '))

frh = (csl * 9 + 160 ) / 5

print(f'A temperatura em Celsius é de {csl} que convertida em Fahrenheit será {frh}')

#Faça um programa que calcule a quantidade de litros de combustível consumidos em uma viagem, sabendo-se que o carro tem autonomia de 12 km por litro de combustível. 
# O programa deverá ler o tempo decorrido na viagem e a velocidade média e aplicar as fórmulas: D = T ∗V       L = D /12

temp = float(input('Quanto tempo de viagem em horas: '))

vlc = float(input('Qual a velocidade do carro? '))

dist = temp * vlc

comb = dist / 12

print(f'A distancia percorrida foi de {dist} km, em {temp} hrs e com {comb} litros')

# CRIE UM QUE MOSTRE O DOBRO O TRIPLO E A RAIZ QUADRADA DE UM NUMERO

n2 = int(input('Digite um numero: '))

dob = n2 + n2

trip = n2 * 3

raiz = n2 ** (1/2)

print(f'O dobro do numero digitado é {dob}, seu triplo é {trip} e sua raiz quadrada é {raiz}')


#FAÇA A TABUADA DE UM NUMERO

valor = int(input('Entre com um número para saber a tabuada: '))  
aux = 0  
print('*' * 18)  
print('Tabuada de {}'.format(valor))  
print('*' * 18)  
while(aux <= 10):  
  print('{0} X {1} = {2}'.format(aux, valor, (aux * valor)))  
  aux = aux + 1 

#FAÇA UM PROGRAMA QUE CONVERTA REAL EM DOLAR

real = float(input('Quantos reais você tem? ' ))

cot = float(input('Qual a cotação do dolar? '))

dolar =  real / cot 

print(f'Em dolar você tem U$ {dolar} e em reais R$ {real}')














 
