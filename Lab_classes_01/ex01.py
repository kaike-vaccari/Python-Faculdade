import turtle
import random

quantidade = int(input('Digite quantas figuras você quer:'))

screen = turtle.Screen()
t = turtle.Turtle()
turtle.colormode(255)
t.speed(2)
t.pensize(3)

def posicao_aleatoria():
    return random.randint(-200, 200), random.randint(-100, 100)

def cor_aleatoria():                #função que gera uma cor aleatória para cada figura
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

def janela():                       #abre a janela da turtle
    screen.bgcolor('black')
    screen.setup(width=600, height=400)

class Quadrado:
    def __init__ (self):
        pass 
    def quadrado(self):
        t.color(cor_aleatoria())
        x, y = posicao_aleatoria()
        t.penup()
        t.goto(x, y)
        t.pendown()
        for _ in range(4):
            t.forward(50)
            t.right(90)
class Triangulo:
    def __init__(self):
        pass
    def triangulo(self):
        t.color(cor_aleatoria())
        x, y = posicao_aleatoria()
        t.penup()
        t.goto(x, y)
        t.down()
        for i in range(2):
            t.fd(100)
            t.lt(120)
        t.forward(100)
        t.setheading(0)
    
class Circulo:
    def __init__(self):
        pass

    def circulo(self):
        t.color(cor_aleatoria())
        cor_aleatoria()
        x, y = posicao_aleatoria()
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.circle(30)
        t.setheading(0)
    
janela()

quadrado1 = Quadrado()
triangulo1 = Triangulo()
circulo1 = Circulo()

L = [quadrado1.quadrado, triangulo1.triangulo, circulo1.circulo]

for i in range(quantidade):
    random.choice(L)()
turtle.done()