class username():
    username=[]

def greet_user():
    username = input("Qual o seu nome?  ")
    """Exibe uma saudação simples"""
    print("Hello, " + username.title()+ "!")

greet_user()

def get_formatted_name(first_name, last_name):
    """Devolve um nome completo formatado de modo elegante"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print('\n Por favor informe seu nome: ')
    f_name= input('first_name: ')
    l_name= input('Last name: ')

    formatted_name = get_formatted_name(f_name, l_name)
    print('\n Hello, ' + formatted_name + '!')

    break
