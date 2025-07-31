import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)  

t = turtle.Turtle()
t.speed(5)
t.width(2)
t.hideturtle()

hue = 0

def draw_flower():
    global hue
    for i in range(36):
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.setheading(i * 10)
        color = colorsys.hsv_to_rgb(hue, 1, 1)
        t.color(color)
        t.circle(150)
        hue += 0.01
        if hue > 1:
            hue = 0
for i in range(60):
    draw_flower()
    t.right(3)
    screen.update() 

turtle.done()
