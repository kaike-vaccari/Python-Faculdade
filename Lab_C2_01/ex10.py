# 10. Crie uma função chamada tabuada() que recebe um número e imprime a tabuada de 1 a 10
n = 0
def tabuada():
    n = int(input('Digite um número:'))
    for i in range(1, 11):
        tab = n * i
        print(n, 'x', i, '=', tab)
        i += 1
tabuada()
