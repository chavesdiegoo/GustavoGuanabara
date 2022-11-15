# n=float(input("Insira quanto Dinheiro voce tem na carteira R$: "))
# d=3.27
# e=float(input("Insira o Valor do Euro: "))
# print("Com R${:.2f}, você pode comprar U${:.2f} dollar".format(n, (n/d)))
# #print("Com R${:.2f}, você pode comprar U${:.2f} Euro".format(n, (n/e)))

n=float(input("Insira quanto Dinheiro voce tem na carteira R$: "))
d=n/3.27
print("Com R${:.2f}, você pode comprar U${:.2f} dollar".format(n, d))
