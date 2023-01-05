from datetime import date
anoatual = date.today().year
ano = int(input('Informe o ano de nascimento: '))
idade = anoatual - ano
print('O atleta tem {} anos '.format(idade))
if idade <= 9:
    print ('Atleta de Categoria Mirim')
elif idade >9 and idade <=14:
    print('Atleta Cateroria Infantl')
elif idade >=14 and idade <=19:
    print('Atleta Categoria Junior')
elif idade >19 and idade < 25:
    print('Atleta Categoria Junior')
elif idade > 25:
    print('Atleta Categoria Master')

