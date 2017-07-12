import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(90)
        some_turtle.right(90)

def draw_shape():
    window=turtle.Screen()
    window.bgcolor("blue")
    sasi=turtle.Turtle()
    sasi.shape("arrow")
    sasi.color("red")
    for i in range(1,37):
        draw_square(sasi)
        sasi.right(10)
        sasi.speed(4)

    window.exitonclick()

draw_shape()
