# FAÇA UM PROGRAMA QUE LEIA TRÊS NÚMEROS E MOSTRE QUAL É O MENOR E O MAIOR

num1 = float(input('Digite um valor: '))
num2 = float(input('Digite um valor: '))
num3 = float(input('Digite um valor: '))


'''if (num1 > num2 or num1 > num3):
    print(f'{num1} é maior')
elif (num2 > num1 or num2 > num3):
    print(f'{num2}é maior')
else:
    print(f'{num3} é maior')'''

if num1 >= num2 and num1 >= num3:
    maior = num1
elif num2 >= num1 and num2 >= num3:
    maior = num2
else:
    maior = num3



if num1 <= num2 and num1 <= num3:
    menor = num1
elif num2 <= num1 and num2 <= num3:
    menor = num2
else:
    menor = num3

print(f'O maior número é: {maior:.2f}')
print(f'O menor número é: {menor:.2f}')