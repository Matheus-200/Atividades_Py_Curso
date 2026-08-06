#  Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc
num = float(input("Digite um valor: "))
print('O valor digitado foi {} e o seu numero inteiro é: {}'.format(num,trunc(num))) 



''' POSSO ULTILIZAR O INT TAMBEM '''
num = float(input("DIGITE AQUI SEU O VALOR: "))
print("O valor digitado foi {}, e seu inteiro é {}".format(num, int(num)))
