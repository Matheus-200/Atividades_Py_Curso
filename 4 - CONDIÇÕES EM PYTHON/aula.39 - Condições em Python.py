'''nome = str(input('Digite o seu nome: '))
if (nome == 'matheus'):
    print('Nossa seu {} seu nome é bonito'.format(nome))
else:
    print('QUE BOSTA DE NOME')
#print('Olá, seja bem vindo {}.'.format(nome))
'''

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.2f}'.format(m))

if (m >= 60):
    print('APROVADO!')
else:
    print('REPROVADO!')