#EXERCICOS DA PAGINA 69 DO LIVRO PYTHON PARA INICIANTES - NOVATEC
#TENTAREI FAZER OS EXERCICIOS DESSA PAGINA COM ABORDAGEM DE CLASSES COM ORIENTAÇÃO A OBJETOS


#RESOLUÇÃO DOS EXERCIOS 2.3 , 2.4, 2.5 E 2.6 DA PAG. 69
class Names:
    def __init__(self, name):
        self.name = name
        
    def message(self):
        print(f'Alô, {self.name.title()}, você gostaria de aprender um pouco de Python?')

    def print_name(self):
        print(self.name.upper())
        print(self.name.lower())
        print(self.name.title())

    def citacao(self, frase, famous_person = 'Steve Jobs'):
        self.frase = frase
        self.famous_person = famous_person
        print(f'{self.famous_person} disse: {self.frase}')

name = input('Qual o seu nome? ')
name = Names(name)
name.message()
name.print_name()
name.citacao('“Seu tempo é limitado, não o perca vivendo a vida de outra pessoa”.\n')

# EXERCICOS DA PAG. 83 LISTA[] 

class Nomes:
    def __init__(self, nomes):
        self.nomes = []
        pass

    def adicionar_nomes(self, nomes):
        while True:
            nome = input('Digite o nome dos seus amigos ou digite 0 para parar: ')
            if nome == '0':
                break
            self.nomes.append(nome)
    def exibir_nomes(self):
        for nome in self.nomes:
            print(nome.title())

    def saudacao(self):
        for nome in self.nomes:
            print(f'Olá {nome.title()}, tudo bem com você?')
    

nomes = Nomes([])
nomes.adicionar_nomes(nomes)
nomes.exibir_nomes()
nomes.saudacao()

class Transportes:
    def __init__(self, transportes):
        self.transportes = []
    
    def add_transportes(self, transportes):
        while True:
            transportes = input('\nDigite o nome do seu transporte ou 0 para sair: ')
            if transportes == '0':
                break
            self.transportes.append(transportes)
    
    def exibir_transportes(self):
        for transporte in self.transportes:
            print(transporte.title())
    
    def message(self):
        for transporte in self.transportes:
            print(f'\nOlá eu gostaria de ter um {transporte.title()}')

transportes = Transportes([])
transportes.add_transportes(transportes)
transportes.exibir_transportes()
transportes.message()

#EXERCICIOS DA PAG. 90

class Listas:
    def __init__(self, listas):
        self.listas = []

    def add_listas(self):
        while True:
            lista = input('Digite o nome do seu convidado ou 0 para sair: ')
            if lista == '0':
                break
            self.listas.append(lista)

    def exibir_listas(self):
        for lista in self.listas:
            print(lista.title())

    def message(self):
        for lista in self.listas:
            print(f'\nOlá gostaria de contar com sua presença no meu evento {lista.title()}')

    def remove_listas(self):
        while True:
            lista = input('Digite o nome do convidado que não poderá vir ou 0 para sair: ')
            if lista == '0':
                break
            if lista in self.listas:
                self.listas.remove(lista)
            else:
                print(f'{lista} não está na lista.')

listas = Listas([])
listas.add_listas()
listas.exibir_listas()   
listas.message()
listas.remove_listas()
listas.add_listas()
listas.exibir_listas()   
listas.message()

#EXERCICIOS DA PAG.94

class Viagem:
    def __init__(self, viagem):
        self.viagem =[]

    def add_viagem(self):
        while True:
            viagem = input('Digite o lugar para onde deseja viajar ou 0 para sair:  ')
            if viagem == '0':
                break
            self.viagem.append(viagem)
    
    def exibir_viagem(self):
        for viagem in self.viagem:
            print(viagem.title())
    
    def message(self):
        for viagem in self.viagem:
            print(f'\nOlá eu vou conhecer {viagem.title()}!')
        
viagem = Viagem([])
viagem.add_viagem()
viagem.exibir_viagem()
viagem.message()

