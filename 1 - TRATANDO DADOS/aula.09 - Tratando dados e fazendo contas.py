#CALCULANDO A MÉDIA DE 4 NÚMEROS
print('VAMOS CALCULAR A MÉDIA DE QUATRO NUMEROS')
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
n3 = int(input('Digite um valor: '))
n4 = int(input('Digite um valor: '))

soma = (n1 + n2 + n3 + n4)

result = soma / 4 

print('A média da soma de {}, {}, {}, e {}, é {:.3f}'.format(n1,n2,n3,n4,result))


