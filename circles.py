import turtle

def draw_shape():
    window=turtle.Screen()
    window.bgcolor("green")
    sasi=turtle.Turtle()
    sasi.shape("arrow")
    sasi.color("red")
    for i in range (1,37):
        sasi.circle(70)
        sasi.right(10)

draw_shape()
        
