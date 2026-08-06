# CONTANDO QUANTAS VEZES UMA LETRA APARECE EM UM TEXTO

nome = str(input('Digite seu nome:' )).strip().lower()
print('A letra (a) aparece: {} vezes na frase escrita'.format(nome.count('a')))
print('A letra A aparece na primeira vez na posição: {}'.format(nome.find('a')  + 1))
print('A letra A aparece pela ultima vez na posição: {}'.format(nome.rfind('a') + 1))