from turtle import Turtle, Screen
# keyword Module_name keyword Thing_in_module

timmy_the_turtle = Turtle()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

# Drawing a box
# for i in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)

# Drawing Dashed Lines
for tim in range(10):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()





# Drawing different shapes

# num_size=5

# for _ in range(num_size):
#     angle=360/num_size
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(angle)





def draw_shape(num_sides):
    angle=360/num_sides
    for _ in range(num_sides):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)

for shape_side_n in range(3,11):
    draw_shape(shape_side_n)



screen = Screen()
screen.exitonclick()
