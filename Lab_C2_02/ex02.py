import turtle
import random

def cor_aleatoria():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
def posicao_aleatoria():
    return random.randint(-300, 300), random.randint(-300, 300)

t =  turtle.Turtle()
turtle.colormode(255)
t.speed(0)

vezes = int(input('Digite quantos quadrados você quer:'))
lado = int(input('Agora digite o valor do lado:'))

for _ in range(vezes):
    x, y = posicao_aleatoria()
    cor = cor_aleatoria()
    tamanho = random.randint(0, 11)

    t.pensize(tamanho)
    t.color(cor)
    t.penup()
    t.goto(x, y)
    t.pendown()

    for _ in range(4):
        t.forward(lado)
        t.rt(90)

turtle.done()