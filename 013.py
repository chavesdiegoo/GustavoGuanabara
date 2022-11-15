s=float(input("Insira o valor do Salario do Funcionario R$: "))
print('Considerando o bonus de 15% o novo salario do colaborador é :',s+(s*15/100))

#outro
s=float(input("Insira o valor do Salario do Funcionario R$: "))
sa = s+(s*15/100)
print('Um funcionario que recebe R${}, com um bonus de 15%, tem o novo salario de: {}'.format(s, sa))

#Bonus
p=float(input("Insira o valor do Preçp do produto  R$: "))
pa= p-(p*5/100)
pd= p+(p*8/100)
print('O produto tem o valor de R${:.2f}. \n Para pagamento a vista o valor é {:.2f}, \n a prazo é de R${:.2f}'.format(p, pa, pd))


