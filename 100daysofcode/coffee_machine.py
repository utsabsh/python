MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0  # Stores total earnings from coffee sales
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Checks if there are enough resources to make the requested drink."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    """Prompts the user to insert coins and calculates the total amount."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Checks if the inserted money is sufficient for the drink."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")  # Provide change if overpaid
        global profit
        profit += drink_cost  # Update total earnings
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")  # Refund if insufficient funds
        return False


def make_coffee(drink_name, order_ingredients):
    """Deducts required ingredients from available resources and serves coffee."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


# Main program loop
is_on = True

while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False  # Turn off the coffee machine
    elif choice == "report":
        # Print available resources and earnings
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif choice in MENU:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("Invalid input. Please choose a valid option.")  # Handle incorrect inputs
