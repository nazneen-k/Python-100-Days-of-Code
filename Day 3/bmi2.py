# Body Mass index 
# BMI= weight(kg)/height^2(m^2)

weight=int(input())
height=float(input())

bmi=(weight/(height*height))
print("BMI = ",bmi)

if(bmi<18.5):
    print(f"your bmi is {bmi}, you are underwight")
elif(bmi<25):
    print(f"Your bmi is {bmi}, you are having normal weight")
elif(bmi <30):
    print(f"You are bmi is {bmi}, you are slightly overweight")
elif(bmi<35):
    print(f"Your bmi is {bmi}, you are obese")
else:
    print(f"Your bmi is {bmi}, you are clinically obese")