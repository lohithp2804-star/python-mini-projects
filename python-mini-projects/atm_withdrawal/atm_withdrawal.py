#ATM cash withdrawal
from getpass import getpass
Withdraw_Amount = int(input("enter withdrawal amount: "))
Balance = 1000
if (Balance>=Withdraw_Amount):
    PIN = getpass("Enter PIN: ")
    if (PIN == "2804"):                                          #PIN Mentioned
        print("Transaction successful")
    else:
        print("Invalid PIN")
else:
    print("Insufficient Balance")