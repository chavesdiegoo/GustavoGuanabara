casa = float(input('Informe o Valor da Casa : R$ '))
salario = float(input('Informe o salario do comprador: R$:'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa /(anos*12)
print('Para pagar uma casa de de R$ {:.2f} em {} anos,'.format(casa, anos), end ='')
print(' a prestação sera de R$ {:.2f} reais' .format(prestacao))
minimo = salario * (30/100)
# print('COMPARANDO {:.2f},{:.2f}' .format(prestacao, minimo))
if prestacao <= minimo:
    print('Empréstimo aprovado')
else:
    print ('Empréstimo Negado')
