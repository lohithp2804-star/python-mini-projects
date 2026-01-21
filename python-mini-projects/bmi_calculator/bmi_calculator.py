#BMI CALCULATOR
weight = int(input("enter your body weight..?"))
height  = float(input("enter your height in meters...?"))
BMI = round(weight//(height**2))
if (BMI <= 18.4):
    print(f"your BMI is {BMI} and you come under underweight")
elif (BMI<24.9):
        print(f"your BMI is {BMI} and you come under normal range")
elif (BMI<29.9):
    print(f"your BMI is {BMI} and you come under overweight")
else:
        print(f"your BMI is {BMI} and you come under obese")