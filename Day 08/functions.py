# Functions with more than one argument
def greet_with(name,location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Angela","London")


# Positional Arguments

# Functions with keyword arguments
def keyword_arguments(a=1,c=3,b=2):
    print(f"C={c}")
    print(f"b={b}")
    print(f'a={a}')

keyword_arguments()