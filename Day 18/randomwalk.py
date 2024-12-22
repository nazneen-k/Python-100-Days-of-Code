import turtle as t
import random

tim = t.Turtle()

colours=["CornflowerBlue","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen","Pink","yellow"]
directions=[0,90,180,278]
tim.pensize(15)
tim.speed("fastest")

for _ in range(50):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))
