import turtle
import random

# Configurações iniciais
quantidade = int(input('Digite quantas figuras você quer: '))
screen = turtle.Screen()
t = turtle.Turtle()
turtle.colormode(255)
t.speed(2)
t.pensize(3)
screen.bgcolor('black')
screen.setup(width=600, height=400)

def posicao_aleatoria():
    return random.randint(-200, 200), random.randint(-100, 100)

def cor_aleatoria():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

def quadrado():
    t.color(cor_aleatoria())
    x, y = posicao_aleatoria()
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    for _ in range(4):
        t.forward(50)
        t.right(90)

def triangulo():
    t.color(cor_aleatoria())
    x, y = posicao_aleatoria()
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    for _ in range(3):
        t.forward(100)
        t.left(120)

def circulo():
    t.color(cor_aleatoria())
    x, y = posicao_aleatoria()
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.circle(30)

# Lista com as funções de desenho
formas = [quadrado, triangulo, circulo]

# Sorteio e desenho
for _ in range(quantidade):
    random.choice(formas)()

turtle.done()
