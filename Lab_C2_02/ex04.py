from turtle import Turtle, pensize, hideturtle, penup, goto, pendown, circle, speed, done
from time import sleep
vezes = int(input('Digite  quantas voltas você quer:'))
velocidade = int(input('Digite o tempo de espera em segundos:'))

t = Turtle()
t.pensize(1)
speed(0)
hideturtle()

raio_inicial = 20
aumento_raio = 20
for i in range(vezes):
    penup()
    goto(0, -raio_inicial - i * aumento_raio)  # centraliza o círculo
    pendown()
    circle(raio_inicial + i * aumento_raio)
    sleep(velocidade)

done()