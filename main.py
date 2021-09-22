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

resources = {
    "water": 300,
    "milk": 300,
    "coffee": 300,
}

acceptance = ['espresso', 'latte', "cappuccino", "off", "report"]
profit = 0


def espresso():
    ingredients = MENU['espresso']['ingredients']
    cost = MENU['espresso']['cost']
    return ingredients, cost


def latte():
    ingredients = MENU['latte']['ingredients']
    cost = MENU['latte']['cost']
    return ingredients, cost


def cappuccino():
    ingredients = MENU['cappuccino']['ingredients']
    cost = MENU['cappuccino']['cost']
    return ingredients, cost


def resources_check(data):
    if data[0]['water'] > resources['water']:
        if data[0]['coffee'] > resources['coffee']:
            print(data[0])
            if 'milk' in data[0].keys() and data[0]['milk'] > resources['milk']:
                return "water and milk and coffee"
            else:
                return "water and coffee"
        return "water"
    elif data[0]['coffee'] > resources['coffee']:
        if 'milk' in data[0].keys() and data[0]['milk'] > resources['milk']:
            return "milk and coffee"
        return "coffee"
    elif 'milk' not in data[0].keys():
        return False
    else:
        if data[0]['milk'] > resources['milk']:
            return "milk"
        else:
            return False


def sub(data):
    for k, v in data[0].items():
        resources[k] = resources[k] - v
    return resources


def money_check(data):
    if money > data[1]:
        return True
    else:
        return False


def output():
    if selection == "espresso":
        data = espresso()
        return data
    elif selection == "latte":
        data = latte()
        return data
    elif selection == "cappuccino":
        data = cappuccino()
        return data
    else:
        return False


def power():
    global power_on
    power_on = False


def report():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}")


def coins(data):
    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    change = total - data[1]
    return total, change


power_on = True
while power_on:
    selection = input("What would you like? (espresso/latte/cappuccino) ")
    while selection not in acceptance:
        selection = input("What would you like? (espresso/latte/cappuccino) ")
    out = output()
    if out:
        res_check = resources_check(out)
        if not res_check:
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickels = int(input("How many nickels? "))
            pennies = int(input("How many pennies? "))
            money = coins(out)
            if money[1] >= 0:
                profit += out[1]
                updated_resources = sub(out)
                resources = updated_resources
                print(f"Here's your {round(money[1], 2)} in change.")
                print(f"Here's your {selection} ☕. Enjoy!")
            else:
                print(f"Not enough money. {money[0]} refunded")
        else:
            print(f"Sorry there is not enough {res_check}")
    elif selection == "report":
        report()
    else:
        power()


