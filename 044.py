preco = float(input('Informe o Valor da Compra R$: '))
print('''Escolha a forma de pagamento: )
[ 1 ] - A vista / dinheiro / cheque
[ 2 ] - a vista cartão
[ 3 ] - em ate 2x no cartão
[ 4 ] - 3x ou mais no cartao''')
opcao = int(input('Escolha a opcao: '))

if opcao ==1:
    total = preco - (preco * 10/100)
    print('o Valor da sua compra com desconto é de de {} reais '.format(total))
elif opcao == 2:
    total = preco - (preco * 5 / 100)
    print('o Valor da sua compra com desconto é de de {} reais '.format(total))
elif opcao == 3:
    total = preco
    parcela = total/2
    print('Sua compra sera parcelada em 2x de R${:.2} '.format(parcela))

elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input('Quantas parcelas?: '))
    print('o Valor da sua compra com juros é de de {} reais '.format(total))
else:
    total = 0
    print('Opção Invalida de Pagamento')