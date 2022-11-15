p=int(input("Insira o preco do produto R$: "))
print("O Valor do produto é R${} reais, com desconto o novo valor é: {}".format(p, p-(p*5/100)))

#outromodo

p=int(input("Insira o preco do produto R$: "))
novo = p-(p*5/100)
print("O Valor do produto é R${:.2f} reais, com desconto o novo valor é R$:{:.2f}".format(p, novo))
