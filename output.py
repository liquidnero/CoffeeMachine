import menu

def espresso():
    ingredients = menu.MENU['espresso']['ingredients']
    cost = menu.MENU['espresso']['cost']
    return ingredients, cost


def latte():
    ingredients = menu.MENU['latte']['ingredients']
    cost = menu.MENU['latte']['cost']
    return ingredients, cost


def cappuccino():
    ingredients = menu.MENU['cappuccino']['ingredients']
    cost = menu.MENU['cappuccino']['cost']
    return ingredients, cost

def main(user_selection):
    if user_selection == "espresso":
        data = espresso()
        return data
    elif user_selection == "latte":
        data = latte()
        return data
    elif user_selection == "cappuccino":
        data = cappuccino()
        return data
    else:
        return False
