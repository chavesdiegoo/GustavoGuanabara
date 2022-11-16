nome=str(input('Insira uma frase: ')).strip().upper()
print('A Letra A aparece {} vezes na frase:'.format(nome.count('A')))
print('A primeira letra A, aparece na posição {}'.format(nome.find('A')+1))
#rfind busca da direita para esquerda
print('A ultima letra A, apareceu na posicao {}'.format(nome.rfind('A')+1))