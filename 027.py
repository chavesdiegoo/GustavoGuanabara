nome = str(input('Insira seu nome completo: ')).strip().upper()
n=nome.split()
#print(n)
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu primeiro nome é {}'.format(n[len(n)-1]))
