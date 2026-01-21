#leap year calculator
year = int(input("enter any year to check wheather it is leap year or not..? "))
if (year%4==0):
    if(year%100==0):
        if (year%400==0):
            print(f"the entered year {year} is 100% a leap year ")
        else :
            print(f"the entered year {year} is not a leap year")
    else:
        print(f"the entered year {year} is 100% a leap year")
else :
    print(f"the entered year {year} is not a leap year")