import turtle



def draw_triangle(some_triangle):

 
    some_triangle.forward(100)
    some_triangle.right(135)
    some_triangle.forward(100)
    some_triangle.right(115)
    some_triangle.forward(90)

    

# def draw_art():


window = turtle.Screen()
window.bgcolor("red")
alex=turtle.Turtle()
alex.shape("turtle")
alex.color("yellow")
alex.speed(2)
for i in range(1,37):
    draw_triangle(alex)
    alex.right(10)





