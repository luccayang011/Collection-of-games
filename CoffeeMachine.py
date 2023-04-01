MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
def check_resource(drink, resource):
    """Returns true when there is enough resources, or false if not."""
    ingredients = drink["ingredients"]
    for ingredient in ingredients:
        if ingredients[ingredient] > resource[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
        else:
            return True


def coin_process(drink):
    """Returns true if the transaction is successful."""
    print("Please insert coins.")
    q = int(input("How many quarters?: "))
    d = int(input("How many dimes?: "))
    n = int(input("How many nickles?: "))
    p = int(input("How many pennies?: "))
    total_coin = p * 0.25 + d * 0.1 + n * 0.05 + p * 0.01
    if total_coin < drink["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif total_coin > drink["cost"]:
        change = round(total_coin - drink["cost"], 2)
        print(f"Here is ${change} dollars in change.")
        return True
    else:
        return True


def make_coffee(order, resource):
    drink = MENU[order]
    ingredients = drink["ingredients"]
    resource["water"] -= ingredients["water"]
    resource["milk"] -= ingredients["milk"]
    resource["coffee"] -= ingredients["coffee"]
    global profit # using the global function to call the variable defined earlier
    profit += drink["cost"]
    return f"Here is your {order}!"


should_continue = True
order = input("What would you like? (espresso/latte/cappuccino): ").lower()

while should_continue:
    if order == 'off':
        should_continue = False
    elif order == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    else:
        sufficient_resource = check_resource(MENU[order], resources)
        if sufficient_resource:
            coin_sufficient = coin_process(MENU[order])
            if coin_sufficient:
                print(make_coffee(order, resources))
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()
