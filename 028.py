from random import randint
computador = randint(0,5)
print ('Vou pensar em um número, entre 0 e 5. Cê é bichão para acertar?')
player = int(input('Em que número eu pensei? '))
if player == computador:
    print('Acerto miseravel')
else:
    print('Ai que burro" Dá Zero para ele" Eu pensei no numero {} e não do {}'.format(computador, player))