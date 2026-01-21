#Love Calculator
name_01 = input("enter your name..? ")
name_02 = input("enter him\her name..? ")
combine = name_01 + name_02
lower_case = combine.lower()
t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")
l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")
true = (t+r+u+e)
love = (l+o+v+e)
love_calcus = int(str(true)+str(love))
print(f"Your love is {love_calcus} stronger")

if (love_calcus<10 or love_calcus>90):
    print("the love between you 2 is like a blast")
elif (love_calcus >=10 and love_calcus <=80):
        print("you both are just good together")
else:
    print("you both are just made for each other")