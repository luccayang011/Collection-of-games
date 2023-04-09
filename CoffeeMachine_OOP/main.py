from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


machine_on = True
menu = Menu() # need to create an object first
coffee = CoffeeMaker()
money = MoneyMachine()

while machine_on:
    # Prompt user by asking “What would you like? (espresso/latte/cappuccino/):”
    order_name = input(f"What would you like? {menu.get_items()} :").lower()
    # Turn off the Coffee Machine by entering “off” to the prompt.
    if order_name == "off":
        machine_on = False
    # Print Report
    elif order_name == "report":
        coffee.report()
        money.report()
    else:
        drink = menu.find_drink(order_name)
        # Check resources sufficient
        if coffee.is_resource_sufficient(drink):
            # Process coins
            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)
