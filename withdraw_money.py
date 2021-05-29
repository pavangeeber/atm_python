import sys
import json

# takes the selected user dictionary entry as parameter from the calling funtion/file (or main?)
user_info=json.loads(sys.argv[1])# !!!DOES NOT WORK!!! Alternate to be checked

amount=input("Enter amount to dispense:")
amount=int(amount)
for acc_balance in user_info:
    if (amount <= user_info[acc_balance]):
        print("Please collect cash, Thanks for using our ATM!")
    else:
        print("Insufficient balance")
user_info[acc_balance]-=amount #how to return this value to the calling funtion to update acc_balance in the original dictionary?


