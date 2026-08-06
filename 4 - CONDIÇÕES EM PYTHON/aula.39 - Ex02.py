#ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO

speed = float(input('Digite a velocidade do seu veiculo: '))
limit = 80
if(speed < limit):
    print('Você está dentro do limite de velocidade')
elif(speed == limit):
    print('Cuidado, você esta no limite de velocidade')
else:
    print('Você ultrapassou o limite permitido!')
    multa = speed - limit
    valor = multa * 7
    print('O valor da sua multa é de: {:.2f}'.format(valor))