num = int(input('Digite um número:'))
if num % 2 == 0:
    pi = ('par')
else:
    pi = ('impar')
if num > 0:
    pn = ('positivo')
elif num < 0:
    pn = ('negativo')
else:
    pn = ('nulo')
print('O número {} é {}, e ele é {}'.format(num, pi, pn))
