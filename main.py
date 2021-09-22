import output

resources = {
    "water": 300,
    "milk": 300,
    "coffee": 300,
}

acceptance = ['espresso', 'latte', "cappuccino", "off", "report"]
profit = 0

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


def teardown():
    global power_on
    power_on = False
    print("Bye!")

def report():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}")


def coins(data):
    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    change = total - data[1]
    return total, change

power_on = True

while power_on:
    selection = input("What would you like? (espresso/latte/cappuccino/report/off) ")
    out = output.main(selection)
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
        teardown()


