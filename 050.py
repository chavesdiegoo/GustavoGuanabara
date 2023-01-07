soma = 0
cont = 0
for c in range(1,7):
        n = int(input('Insira o primeiro valor: '))
        if n%2 == 0:
            soma = soma +n
            cont = cont +1
print('Voce digitou {} pares, e a soma dos 6 intervalos é {}'.format(cont, soma))