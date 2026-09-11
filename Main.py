# Restaurant Bill Splitter Program
# Simple Bill Splitter Program made in my Intro to Programming I class CS101

import time 

def Main():
    print("===== BILL =====")

    people = 0

    while people <=0:
        try:
            bill = float(input("\nEnter the bill amount($):"))
            if bill < 0 or bill == 0:
                print("\nBill Needs to be greater than 0. Restarting Try Again!")
            else:
                people = int(input("\nEnter the number of people:"))
                if people <=0:
                    print("\nNumber of people must be greater than 0. Restarting Try Again!")
                elif people <=-0:
                    print("\nPlease enter a valid number")
                else:
                    print(f"\nAdding bill amount which is ${bill} and {people} together. Please wait...")
                    time.sleep(5)
                    print("\nAdded Successfully")
                    break
        except ValueError:
            print("\nNeeds to be numbers only! Restarting Try Again!")
    percentage = float(input("\nEnter the amount of tip (%):"))
    total = bill + (bill * percentage / 100)
    amount = total / people

    print(f"Total bill after tip ($): {total:.2f}")
    print(f"With having {people} people")
    print(f"Each person will pay ($): {amount:.2f}")
    print("Thank you for using our app!")

Main()