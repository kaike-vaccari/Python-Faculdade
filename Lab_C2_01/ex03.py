# 3. Crie uma função chamada quadrado() que recebe um número e imprime o quadrado dele
num = 0
quad = 0
def quadrado():
    num = int(input('Digite um número:'))
    quad = num ** 2
    print('O quadrado de {} é {}'.format(num, quad))
quadrado()