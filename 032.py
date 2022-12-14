from datetime import date
ano = int(input('Infome o ano que deseja analisar: Informe 0 para calcular o ano atual: '))
if ano ==0:
    ano = date.today().year
if ano%4 == 0 and ano%100 != 0 or ano%400 ==0:
    print('O ano de {} é um ano bisexto '.format(ano))
else:
    print('O ano de {} não é um ano bisexto '.format(ano))