# Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas

Km = float(input('Escreva a distância: '))
valor1 = 0.50
valor2 = 0.45
Limite = 200
if (Km > Limite):
    print('O valor da viagem é de: {:.2f}'.format(Km * valor2))
else:
    print('O valor da viagem é de: {:.2f}'.format(Km * valor1 ))