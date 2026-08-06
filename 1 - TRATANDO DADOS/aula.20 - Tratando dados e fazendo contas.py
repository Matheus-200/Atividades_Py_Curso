print("Faça um programa que leia um número e mostre na tela o seu sucessor e seu antecessor.")
n1 = int(input("digite um numero: "))
antecessor = n1 - 1
sucessor = n1 + 1

print(" O sucessor de {} é {}, e seu antecessor é {}".format(n1, sucessor, antecessor))

#---------------------------------------------------- 

print("Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz: ")
n1 = int(input("Escreva um valor "))
dobro =  n1 * 2
triplo = n1 * 3
raiz = n1 * n1 
print("O dobro de {} é {}, o triplo é {} e a raiz é {}.".format(n1, dobro, triplo, raiz))

#---------------------------------------------------- 

print ("Escreva um numero que leia um valor em metros e o exiba convertido em centimetros e milimetros: ")

n1 = int(input("Escreva um valor: "))
centimetros = n1 * 100 
milimetros = n1 * 1000

print("{:.3f} centimetros, {:.3f} milimetros".format(centimetros, milimetros))

#---------------------------------------------------- 

print("Faça um programa que leia um numero inteiro e monte sua taboada")
numero = int(input('ESCREVA UM NUMERO'))

for i in range(1,11):
    resultado = numero * i
    print(f" {numero} x {i} = {resultado} " )

#---------------------------------------------------- 
print("Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostres quantos dólares ela pode comprar: " )
us = 3.27
valor = int(input("Digite o valor da sua carteira: "))

resultado = valor / us
print("{:.3f}".format(resultado))

#----------------------------------------------------
print("Faça um programa que leia a altura e largura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la sabendo que cada litro de tinta, pinta uma área de 2m²")
altura = float(input("Digite o valor da altura em metros "))
largura = float(input("Digite o valor da largura em metros "))
tinta = 2

area = altura * largura 
resultado = area / tinta
print("O tamanho da area é {}".format(area))
print("A quantidade de tinta necessária é de {}".format(resultado))

#----------------------------------------------------

print("Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.")
km = float(input("Digite o km do carro: " )) * 0.15
dias = int(input("Digite o dias alugados: " )) * 60
total = km + dias
print("O valor total a pagar é: {:.2f}.".format(total))


