# 8. Crie uma função chamada maior() que recebe dois números e retorna o maior
num1 = 0
num2 = 0
def maior():
    num1 = int(input('Digite um número:'))
    num2 = int(input('Agora digite outro:'))
    maior1 = max(num1, num2)
    print('O maior número é {}'.format(maior1))
maior()