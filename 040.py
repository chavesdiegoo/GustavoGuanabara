n1 = float(input('Entre com a primeira nota: '))
n2 = float(input('Entre com a segunda nota: '))
media = (n1 + n2) / 2
print(media)
if media < 5:
    print('O aluno tirou {:.2} e {:.2}, obtendo a média de {:.2}. '.format(n1, n2, media))
    print('Logo ele esta Reprovado')
elif media >= 5 <= 6:
    print('Logo ele esta Recuperação')
elif media >= 7:
    print('Logo ele esta Aprovado')
