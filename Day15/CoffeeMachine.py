from coffeeMenu import MENU, resources


def report():
    print(f"{water} ml")
    print(f"{milk} ml")
    print(f"{coffee} gm")
    print(f"$ {money}")

# def check_resource():

    # report of resources
is_On = True
# program starts with asking user choice
while is_On:
    answer = input("What would you like? (espresso/latte/cappuccino):")
    if answer == "report":
        print(f"Coffee : {resources['coffee']}")
        print(f"Water: {resources['water']} ml")
        print(f"Milk :{resources['milk']} ml")
        print(f"Money :{resources['money']}")
    elif answer == "off":
        is_On = False
    else:
        print("Invalid Input...")
    # Last message
    print(f"Here is your {answer}. enjoy!")
