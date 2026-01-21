#Roller coaster
height = float(input("enter your height in feets..? "))
if (height>=3.0):
    print("you can ride roller coaster")
    age = int(input("enter your age..? "))
    if age<=5 :
        bill = 250
        print("pay 250 and get your ticket")
    elif age<=12:
        bill = 500
        print("pay 500 and get our ticket")
    elif age<=18:
        bill = 750
        print("pay 750 and get your ticket")
    elif age>18:
        bill = 1000
    selfie = input("do you want to take selfie..? ")
    if (selfie=='yes' or 'Yes' or 'YES'):
        Bill = bill+50
        print(f"your total bill is {Bill}")
    else:
        Bill = bill+0
        print(f"your bill is {Bill}")
else:
    print("you cant ride roller coaster")
print("Happy vacation")