from datetime import date
agora = date.today().year
ano = int(input('Informe o ano de nascimento do candango: '))
idade = agora - ano
print('Quem nasceu em {}, tem hoje {} anos em {} .'.format(ano, idade, agora))
if idade < 18:
    resto = 18 - idade
    print('Falta pouco, apenas {} anos '.format(resto))
elif idade ==18:
        print('Ta na hora')
else:
    resto = idade - 18
    print('passou da idade, em {} anos '.format(resto))
