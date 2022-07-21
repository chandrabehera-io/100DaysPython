from secrets import choice
from coffeeMenu import MENU, resources


def is_resource_sufficient(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return is_enough  # 14:00 time


def process_coins():
    """Returns Total Money, Calculated from coins inserted"""
    print("Please insert coins:")
    total = int(input("How many Quarters? :")) * 0.25
    total += int(input("How many Dimes? :")) * 0.1
    total += int(input("How many Nickles? :")) * 0.05
    total += int(input("How many Pennies? :")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is $ {change} in change .")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money Refunded...!!!")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deducts ingredients from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}.")


is_On = True
profit = 0
# program starts with asking user choice
while is_On:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "report":
        print(f"Coffee : {resources['coffee']}")
        print(f"Water: {resources['water']} ml")
        print(f"Milk :{resources['milk']} ml")
        print(f"Money :{profit}")
    elif choice == "off":
        is_On = False
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
