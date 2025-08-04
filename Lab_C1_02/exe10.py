n1 = int(input('Digite um número:'))
n2 = int(input('Agora digite outro:'))
n3 = int(input('Mais um:'))
L = [n1, n2, n3]
nmax = max(L)
if nmax % 2 == 0:
    print('O maior número entre eles é {}, e esse número é par'.format(nmax))
else:
    print('O maior número entre eles é {}, e esse número é impar'.format(nmax))
