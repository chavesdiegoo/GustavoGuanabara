#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.
from math import sqrt
c1= float(input('Insira o comprimento do cateto oposto: '))
c2 = float(input('Insira o comprimento do cateto adjacente: '))
h= (c1**2)+(c2**2)
print('A hipotenusa é {}'.format(sqrt(h)))
