n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro numero: '))
s = n1 + n2
print(f'A soma entre {n1} e {n2} vale',s)


n3=int(input('Digite um numero: '))
n4= int(input('Digite outro numero: '))
sb = n3 - n4

print(f'A subtração entre {n3} e {n4} vale', sb)

n5=str(input('Digite algo: '))
print(type(n5))
print('Só tem espaços? ', n5.isspace())
print('É um numero? ', n5.isnumeric())
print('É alfabetico? ',n5.isalpha())
print('É alfanumerico? ', n5.isalnum())
print('Esta em maiscula? ',n5.isupper())
print('Esta em minuscula? ',n5.islower())
print('Esta capitalizada? ',n5.istitle())




