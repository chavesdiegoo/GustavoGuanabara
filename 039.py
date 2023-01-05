from datetime import date
agora = date.today().year
ano = int(input('Informe o ano de nascimento: '))
idade = agora - ano
print('Quem nasceu em {}, tem hoje {} anos em {} .'.format(ano, idade, agora))
if idade ==18:
        print('Ta na hora')
elif idade < 18:
    resto = 18 - idade
    c = agora + resto
    print('Falta pouco, apenas {} anos '.format(resto))
    print('Seu alistamento será em {}'.format(c))
else:
    resto = idade - 18
    c = agora - resto
    print('passou da idade, em {} anos '.format(resto))
    print('Seu alistamento foi em {}'.format(c))

