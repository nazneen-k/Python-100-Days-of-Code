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


screen = Screen()
screen.exitonclick()


