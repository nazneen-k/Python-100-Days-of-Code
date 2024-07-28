# # Range
# The range() function has three forms of syntax:

# range(stop): Generates a sequence from 0 up to stop - 1.
# range(start, stop): Generates a sequence from start up to stop - 1.
# range(start, stop, step): Generates a sequence from start to stop - 1, incrementing by step.

for number in range(5):
    print(number)

for number in range(1,10):
    print(number)

for number in range(1,10,2):
    print(number)

# Sum of numbers
total=0
for number in range(1,10):
    total+=number
print(total)


# Sum of even numbers
print("Sum of Even Numbers:")
sumOfEvenNumbers=0
for number in range(0,10+1,2):
    sumOfEvenNumbers+=number
print(sumOfEvenNumbers)