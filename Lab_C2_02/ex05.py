#Exercício 5 – Controle com Teclado
import turtle

t = turtle.Turtle()
t.pensize(2)
t.speed(0)
t.shape('turtle')

def mover_para_cima():
    t.setheading(90)
    t.forward(20)
    
def mover_para_direita():
    t.setheading(0)
    t.forward(20)

def mover_para_esquerda():
    t.setheading(180)
    t.forward(20)

def mover_para_baixo():
    t.setheading(270)
    t.forward(20)

turtle.listen()
turtle.onkey(mover_para_direita, 'Right')
turtle.onkey(mover_para_cima, 'Up')
turtle.onkey(mover_para_esquerda, 'Left')
turtle.onkey(mover_para_baixo, 'Down')

turtle.done()
