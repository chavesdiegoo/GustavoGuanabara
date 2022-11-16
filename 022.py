# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome=str(input('Insira seu nome: ')).strip()
print('Analisando seu nome...')
print('Nome em maiusculo é :{} '.format(nome.upper()))
print('Nome em Minúsculo é :{} '.format((nome.lower())))
print('Tamanho da frase considerando espaços antes e depois: ',(len(nome)))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
divisao = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(divisao[0], len(divisao[0])))

