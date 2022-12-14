# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Informe a distancia em KM da viagem a ser percorrida: '))
if distancia < 200:
    preco = float (distancia * 0.50)
    print ('Sua viagem de {}KM, terá o Valor da passagem é de R$ {:.2f} Reais. '.format(distancia,preco))
else:
    preco = float (distancia * 0.45)
    print ('Sua viagem de {}KM, terá o Valor da passagem é de R$ {:.2f} Reais. '.format(distancia,preco))