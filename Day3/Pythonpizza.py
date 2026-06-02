#This code is saved to practice the for loop. 


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size != "S" and size != "M" and size != "L":
    print("Thank you for your visit today and we hope you have a great day!")
elif size == "S":
    bill += 15
    print(f"The price of small pizza is $15.0")
    if pepperoni == "Y":
        bill += 2
        print(f"The price of pepperoni is $2.0")
        if extra_cheese == "Y":
            bill += 1
            print(f"The price of extra cheese is $1.0")
    print(f"Your total bill is ${bill}. Please enjoy your Pizza.")
elif size == "M":
    bill += 20
    print(f"The price of medium pizza is $20.0")
    if pepperoni == "Y":
        bill += 3
        print(f"The price of pepperoni is $2.0")
        if extra_cheese == "Y":
            bill += 1
            print(f"The price of extra cheese is $1.0")
    print(f"Your total bill is ${bill}. Please enjoy your Pizza.")
else :
    bill += 25
    print(f"The price of large pizza is $25.0")
    if pepperoni == "Y":
        bill += 3
        print(f"The price of pepperoni is $2.0")
        if extra_cheese == "Y":
            bill += 1
            print(f"The price of extra cheese is $1.0")
    print(f"Your total bill is ${bill}. Please enjoy your Pizza.")

