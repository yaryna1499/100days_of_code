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
    "Water": 40,
    "Milk": 50,
    "Coffee": 76,
    "Money": 0
}


def compare(drink):
    if MENU[drink]["cost"] > resources["Money"]: print("Sorry there is not enough money.")
    if MENU[drink]["ingredients"]["water"] > resources["Water"]: print("Sorry there is not enough water.")


print(compare("latte"))