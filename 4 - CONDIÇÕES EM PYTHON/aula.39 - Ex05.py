# FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE É BISSEXTO

ano = int(input('ESCREVA O ANO: '))

if ano % 4 == 0 and ( ano % 100 != 0 or ano % 400 == 0):
    print(f'{ano} é bissexto!')
else:
    print('Não é bissexto')