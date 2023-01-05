a = float(input('informe a 1 medida: '))
b = float(input('informe a 2 medida: '))
c= float(input('informe a 3 medida: '))
if a < b + c and b <a +c and c < a+b:
    print('As medidas formam um triangulo ',end='')
    if a == b == c:
        print('Equilatero')
    elif (a == b) or (a == c) or (b == c):
        print("triângulo ISÓSCELES.")
    elif (a != b) or (a != c) or (a != c) :
        print("triângulo Escaleno.")
else:
    print('nao forma triangulo')