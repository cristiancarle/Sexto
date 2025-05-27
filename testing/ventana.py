import turtle  as t
import random

t.speed(0)
t.bgcolor("Black")
colores = ["red","orange", "yellow","green","blue","purple"]
def dibujar_espiral():
    for i in range(360):
        t.pencolor(colores[i%6])
        t.forward(i)
        t.right(60)

dibujar_espiral()
t.hideturtle()
t.exitonclick()