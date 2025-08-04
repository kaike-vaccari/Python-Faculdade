# 9. Crie uma função chamada repetir_mensagem() que recebe uma mensagem e um número n e imprime a mensagem n vezes
n = 0
def repetir_mensagem():
    mensagem = input('Digite uma mensagem:')
    n = int(input('Agora digite quantas vezes você quer que essa mensagem se repita:'))
    i = 0
    while i != n:
        print(mensagem)
        i += 1
repetir_mensagem()