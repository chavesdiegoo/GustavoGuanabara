a = int(input('informe o primeiro valor: '))
b = int(input('informe o segundo valor: '))
c = int(input('informe o terceiro valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('o menor valor informado foi :{}'.format(menor))
maior = a
if b > a and b > c:
    maior = b
if c > a and  c > b:
    maior = c
print('o maior valor informado foi :{}'.format(maior))