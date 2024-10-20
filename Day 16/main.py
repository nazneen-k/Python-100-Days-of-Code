# Object Oriented Programming


# import another_modul e
# print(another_module.another_variable)

# from turtle import Turtle, Screen

# timmy = Turtle()

# print(timmy)
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)
# timmy.left(200)
# timmy.forward(100)
# timmy.right(100)
# timmy.forward(100)


# my_screen = Screen()
# print(my_screen.canvheight)

# my_screen.exitonclick()



from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align="l"

print(table)
table.align="r"
print(table)
