print('='*25)
print('10 TERMOS DE UMA PA')
print('='*25)
termo = int(input('Entre com o Primeiro Termo: '))
razao = int(input('Informe a razão: '))
decimo = termo + (10-1) * razao
for c in range(termo, decimo + razao, razao):
    print('{}'.format(c), end='-')
print('acabou mané')
0