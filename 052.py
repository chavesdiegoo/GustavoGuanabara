n = int(input('Digite o numero: '))
tot = 0
for c in range(1, n +1):
    if n % c ==0:
        print('\033[35m', end='')
        tot = tot +1
    else:
        print('\033[m', end='')
    print('{} '.format(c), end='')
print('O numero {}, foi divisivel {}'.format(n,tot))
if tot ==2:
    print('O numero é PRIMO')
else:
    print('O numero não é PRIMO')



