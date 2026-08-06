# LEIA O NOME COMPLETO DE UMA PESSOA, MOSTRANDO O PRIMEIRO E O ULTIMO NOME
 
nome = str(input('ESCREVA SEU NOME: ')).strip()
n = nome.split()
print('SEU NOME TEM: {}'.format(len(nome) - len(' ')))
print('SEU PRIMEIRO NOME É: {}'.format(n[0]))
print('SEU PRIMEIRO ULTIMO NOME É: {}'.format(n[len(n) - 1]))