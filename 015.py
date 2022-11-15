#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias= float (input("Informa a quantidade de dias de locação: "))
km=float(input('Insira a quantidade de KM percorridos do veiculo alugado: '))

preco_dia = dias * 60
km_rodado = km * 0.15

print("Valor a pagar sobre {} dias de locação, mais {:.2f}km rodados é de: R${:.2f} reais".format(dias, km, preco_dia + km_rodado))

#outroMetodo

dias= float (input("Informa a quantidade de dias de locação: "))
km=float(input('Insira a quantidade de KM percorridos do veiculo alugado: '))
preco_dia = (dias * 60) + (km * 0.15)
print("Valor a pagar sobre {} dias de locação, mais {:.2f}km rodados é de: R${:.2f} reais".format(dias, km, preco_dia))
