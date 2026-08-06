''' calculando a raiz de um valor usando  o import'''
from math import sqrt

numero = int(input("Digite um valor, e vamos calcular a sua raiz: "))

print("A raiz de {}, é: {:.2f}".format(numero, sqrt(numero)))