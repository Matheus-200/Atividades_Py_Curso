#  Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
n1 = str(input('Escreva o nome do  aluno: '))
n2 = str(input('Escreva o nome do  aluno: '))
n3 = str(input('Escreva o nome do  aluno: '))
n4 = str(input('Escreva o nome do  aluno: '))

lista = [n1,n2,n3,n4] 
esolhido = random.choice(lista)
print("O aluno escolhido é:{} ".format(esolhido))
