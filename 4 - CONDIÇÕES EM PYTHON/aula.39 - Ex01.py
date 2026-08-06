# Tentando escolher o mesmo número que a máquina

import random
print('Tente advinhar o número')
maquina = random.randint(1,5)

pessoa = int(input('Digite um valor de 1 a 5:  '))

if (pessoa == maquina):
    print('Parabéns você venceu!')
else:
    print('Você perdeu!')

    print('A máquina escolheu {}'.format(maquina))