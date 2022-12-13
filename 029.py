vel = float(input('Qual a Velocidade atual do Carro? '))
if vel > 80:
    print ('Dirigir a {} KM/H não é seguro. Esta acima do permitido que é 80KM/H. '.format(vel))
    multa = (vel - 80) *7
    print('O valor da Multa é R$ {:.2f} Reais'.format(multa))
else:
    print ('Dirigir a {} KM/H é seguro. Esta dentro do permitido que é 80KM/H. Pilote com segurança '.format(vel))