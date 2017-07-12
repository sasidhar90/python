import turtle
def draw_shape():
    window=turtle.Screen()
    window.bgcolor("yellow")
    sasi=turtle.Turtle()
    times=0
    
    sasi.color("red")
    sasi.shape("circle")
    sasi.speed(2)
    while(times <4): 
        sasi.forward(100)
        sasi.right(90)
        times=times+1

    brad=turtle.Turtle()
    brad.right(180)
    brad.circle(100)
    brad.color("orange")
    brad.shape("turtle")
    

    tesla=turtle.Turtle()
    

    turns=0
    tesla.shape("arrow")
    tesla.forward(80)
    tesla.right(300)
    tesla.forward(80)
    tesla.left(60)
    tesla.forward(80)
    window.exitonclick()

draw_shape()
