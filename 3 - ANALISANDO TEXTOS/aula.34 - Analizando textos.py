''' Crie um programa que leia o nome completo de uma pessoa e mostre algumas informações'''

''''nome = str(input('Digite seu nome: ')).strip()  #estou tirando todos os espaços antes e depois da escrita
print('Seu nome em Maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
print ('Seu nome tem ao todo {} letras'.format(len(nome)- nome.count(' '))) #tirando os espaços entre os nomes'''

# upper (Vai ficar tudo em maiúsculo)
'''nome = str(input('Digite seu nome: '))
print("Seu nome é: {}".format(nome.upper()))
'''
#lower (O nome vai ficar em minúsculo)
'''nome = str(input('Digite seu nome: '))
print("Seu nome vai ficar: {}".format(nome.lower()))'''

#strip() tira os espaços antes e depois da escrita
# count(' ') tira os espços entre as escritas
'''nome = str(input('Digite seu nome: ')).strip()
print('Seu nome contém: {} caracteres.'.format(len(nome) - nome.count(' ')))'''

#len - contando todas as letras escritas 
#count tirando as letras
'''nome = str(input('Teste para remoção de espaços de nomes: ')).strip()
print('O seu nome tem essa quantidade sem as letras: {}'.format(len(nome) - nome.count('e')))'''

nome = str(input('Digite seu nome: ')).strip()
print('Seu primeiro nome contém {} letras'.format(nome.find(' ')))
