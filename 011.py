a=float(input("Entre com a altura da parede: "))
l=float(input("Entre com a Largura da Parede: "))
d =float(a*l)
print('Sua parede tem a dimensão de: {:.2f}m². Para pintar a mesma, é necesario {:.1f}l de tinta'.format(d, (d/2)))

