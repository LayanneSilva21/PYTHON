#IF ELSE

hora = int(input("Que horas são?"))
print(f"Você digitou {hora}")

if hora < 12:
    print ("Bom dia!")
elif hora < 18:
    print("Boa tarde!")
else:
    print("Boa noite!")

#CALCULADORA DE IMC 

peso= float(input("Qual o seu peso?"))
print(f"Seu peso é {peso}")

altura= float(input("Qual a sua altura?"))
print(f"Sua altura é {altura}")

calculo = peso // altura * altura

if calculo <= 18.5:
    print("Abaixo do peso") 
elif calculo <=19:
    print("Peso normal")
elif calculo <= 25:
    print("Sobrepeso")
else:
    print("Obesidade")    

#ESTRUTURA WHILE

x: int

soma: int

soma =0

x= int(input("Digite um numero: "))

while x !=0:
    soma = soma + x
    x= int(input("Digite outro numero: "))

print("Soma = " , soma)


#CALCULADORA 

def soma(x,y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao (x, y): 
    if y != 0:
        return x / y 
    else:
        return "Erro! Divisao por zero"

print("Selecione a operacao: ")
print("1. Soma")
print("2. Subtracao")
print("3. Multiplicacao")
print("4. Divisao")

escolha = input("Digite sua escolha (1/2/3/4)")

num1= float(input("Digite o primeiro número: "))
num2= float(input("Digite o segundo número: "))

if escolha =='1':
    print(f"{num1} + {num2} = {soma(num1, num2)}")
elif escolha =='2':
    print(f"{num1} - {num2} = {subtracao(num1, num2)}")
elif escolha =='3':
    print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")
elif escolha =='4':
    print(f"{num1} / {num2} = {divisao(num1, num2)}")
else:
    print(f"Opção Invalida!")


#INSTRUÇÃO FOR 

N = int(input("Quantos números serão digitados? "))

soma = 0

for i in range(0, N):
    x = int(input("Digite um numero: "))
    soma = soma + x

print("Soma = ", soma)

    