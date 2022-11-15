    #Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
    # Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
    import random
    a = str(input("Insira o nome do Primeiro Aluno: "))
    b = str(input("Insira o nome do Segundo Aluno: "))
    c = str(input("Insira o nome do terceiro Aluno: "))
    d = str(input("Insira o nome do quarto aluno: "))
    lista = [a,b,c,d]
    escolhido = random.choice(lista)
    print('O nome sorteado foi: {}'.format(escolhido))
