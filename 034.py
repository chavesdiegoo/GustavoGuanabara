sal = float (input('informe o salario do colaborador: '))
if sal <= 1250:
    nsal = sal + (sal*15)/100
else:
    nsal = sal + (sal * 10)/100
print('O novo salario do colaborador é de R$ {:.2f} reais '.format(nsal))