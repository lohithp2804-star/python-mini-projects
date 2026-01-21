#pizza order work
order = input("what size of pizza do you need..? ")
cost = 0
if (order == 'small pizza'):
    cost += 100
    print("you have to pay 100")
elif (order == 'medium pizza'):
    cost += 200
    print("you have to pay 200")
elif (order == 'large pizza'):
    cost += 300
    print("you have to pay 300")
pepparani = input("do you need pepparani..? ")
if (pepparani == 'yes'):
    for_which_size = input("for which size do you need")
    if (for_which_size == 'small size') :
        cost += 30
        print(f"your total is {cost}")
    elif (for_which_size == 'medium size') :
        cost +=50
        print(f"your total is {cost}")
    elif (for_which_size == 'large size') :
        cost += 100
        print(f"your total is {cost}")
elif (pepparani == 'no'):
    print(f"its ok") 
cheese = input("do you want extra cheese..?")
if (cheese == 'yes') :
    cost +=20
    print(f"Including extra cheese your total bill is {cost}")
else :
    cost +=0
    print(f"your total bill is {cost}")