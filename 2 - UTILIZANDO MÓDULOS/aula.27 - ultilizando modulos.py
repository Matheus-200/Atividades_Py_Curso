# Faça um programa que leia um angulo qualquer e mostre o valor do seno, cosseno, e tangnte desse angulo:
import math
angulo = float(input('Escreva um angulo: '))

tangente = math.tan(math.radians(angulo))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))

print('Calculando o angulo {:.2f}, o seu seno é: {:.2f}, seu cosseno é: {:.2f}, e o tangente: {:.2f}.'.format(angulo, seno, cosseno, tangente))

