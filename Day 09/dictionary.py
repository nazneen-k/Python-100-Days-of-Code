programming_dictionary = {
    "Bug":"An error in a program that prevents  the program from running as expected",
    "Function":"A piece of code that you can easily call over and over again"
}

print(programming_dictionary["Bug"])

# Adding new items to dictionary
programming_dictionary["Loop"]="The action of doing something over and over again"

print(programming_dictionary)

# Empty Dictionary
empty_dictionary={}

# Edit an item in a dictionary
programming_dictionary["Bug"]="This is the new Bug defination"

print(programming_dictionary)

# Looping through a dictionary
for things in programming_dictionary:
    print(things)
# Output:
# Bug
# Function
# Loop

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Wiping an existing dictionary
programming_dictionary={}
