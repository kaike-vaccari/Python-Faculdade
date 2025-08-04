# 5. Crie uma função chamada par_ou_impar() que recebe um número e imprime se é par ou ímpar
num = 0
def par_ou_impar():
    num = int(input('Digite um número:'))
    if num % 2 == 0:
        print('O número que você digitou é par.')
    else:
        print('O número que você digitou é impar.')
par_ou_impar()