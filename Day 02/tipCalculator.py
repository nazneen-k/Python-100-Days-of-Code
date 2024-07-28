print("Welcome to the tip calculator!")

# Reading input values
bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# Calculating tip as a percentage
tip_as_percent = tip / 100

# Calculating total tip amount
total_tip_amount = bill * tip_as_percent

# Calculating total bill
total_bill = bill + total_tip_amount

# Calculating bill per person
bill_per_person = total_bill / people

# Formatting the result to 2 decimal places
bill_per_person = round(bill_per_person, 2)

print("Each person should pay: ₹", bill_per_person)
