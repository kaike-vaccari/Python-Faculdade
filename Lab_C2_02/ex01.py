import turtle #importa o módulo turtle

t = turtle.Turtle() #cria a turtle
t.pensize(3)
t.speed(1)
t.color('blue')

while True: #laço de repetição para garantir que o usuário digite ou quadrado ou retângulo
    figura = input('Digite se você deseja um quadrado ou retângulo:').lower()
    if figura == 'quadrado':
        lado = int(input('Digite o valor do lado do quadrado:'))
        for _ in range(4):
            t.fd(lado)
            t.rt(90)
        break #quebra o laço de repetição
    elif figura == 'retangulo':
        base = int(input('Digite o valor da base do retangulo:'))
        altura = int(input('Digite o valor da altura do retangulo:'))
        for _ in range(2):
            t.fd(base)
            t.rt(90)
            t.fd(altura)
            t.rt(90)
        break
    else:
        print('Opção inválida. Tente novamente.')

turtle.done() #mantém a janela aberta