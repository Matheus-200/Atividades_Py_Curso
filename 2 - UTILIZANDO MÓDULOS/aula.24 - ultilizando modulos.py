#CALCULANDO A RAIZ QUADRADA DE UM NUMERO ULTILIZANDO MATCH 

import math #importando os calculos matematicos
num = int(input("Escreva um número: ")) 
raiz = math.sqrt(num) #essa função serve para raiz
print("A raiz quadrada de {}, é: {}.".format(num, math.ceil(raiz)))

