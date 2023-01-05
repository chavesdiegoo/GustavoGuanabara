numero = int(input('Insira um numero inteiro a ser convertido: '))
print('''Escolha uma das das bases para conversão:
      [ 1 ] converter para BINARIO
      [ 2 ] converter para Octal
      [ 3 ] converter para Hexadecimal''')
opcao = int(input('Digite a opcao escolhida: '))
if opcao == 1:
    print('{} convertido para Binário é igual a {} '.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido para Binário é igual a {} '.format(numero, oct(numero)[2:]))
elif opcao ==3:
    print('{} convertido para Binário é igual a {} '.format(numero, hex(numero)[2:]))
#     2: tratamento de string, exibe a partir da 3ª casa
else:
    print('Digite apenas as opções acima')
