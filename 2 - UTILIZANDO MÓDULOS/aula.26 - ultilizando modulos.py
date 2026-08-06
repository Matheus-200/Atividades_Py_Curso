'''  FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJACENTE DE UM TRIANGULO RETANGULO, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA'''
# usando o metodo tradicional 
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('a hipotenusa vai medir {:.2f}'.format(hi)) 


'''-----------------------------------'''
# usando o math 
import math
co = float(input('Complimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente:  '))
hi = math.hypot(co, ca)
print("A hipotenusa vai dar: {:.2f}.".format(hi))

''' Calcular a distância entre dois pontos no plano cartesiano (x1, y1) e (x2, y2).'''

x1 = float(input('X do ponto 1: '))
y1 = float(input('Y do ponto 1: '))
x2 = float(input('X do ponto 2: '))
y2 = float(input('Y do ponto 2: '))
distancia = math.hypot(x1 - x2, y1 - y2)
print('a distancia dos catetos vai ser igual a: {}'.format(distancia))