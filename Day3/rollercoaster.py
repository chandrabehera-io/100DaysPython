height = int(input("Enter your Height in cm : "))
bill = 0
if height >= 120:
    print("You can ride rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        photo = input("Do you want a photo? ")
        print("Ticket price is $5 ")
    elif age > 12 and age <= 18:
        bill = 7
        print("Ticket price is $7 ")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Ticket is on the house")
    else:
        bill = 15
        print("Ticket price is $15 ")

    want_photo = input("Do you want a photo? Y or N : ")
    if(want_photo == "Y"):
        if(age >=45 and age<=55):
            print("Your total bill is on the house")
        else:
            bill += 3
            print(f"Your total bill is ${bill}")
else:
    print("You cannot ride rollercoaster")
