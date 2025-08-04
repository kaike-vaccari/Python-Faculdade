import turtle
v = int(input('Digite quantas vezes você quer que o zig zag aconteça:'))
L = ['blue', 'orange', 'grey', 'green', 'red', 'purple', 'yellow', 'black', 'pink', 'brown']

t = turtle.Turtle()
t.pensize(3)
t.speed(2)

t.up()
t.goto(-380, 0)
t.down()

i = 0
t.rt(45)
for _ in range(v):
    if i > 9:
        i = 0
    t.color(L[i])
    t.lt(90)
    t.fd(100)
    i += 1
    t.color(L[i])
    t.rt(90)
    t.fd(100)
    i += 1

turtle.done()
