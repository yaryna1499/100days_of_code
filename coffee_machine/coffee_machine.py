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
    "Water": 100,
    "Milk": 50,
    "Coffee": 76,
    "Money": 2.5
}


while True:
    choice = input(" What would you like? (espresso/latte/cappuccino)")

    drinks = ["espresso", "latte", "cappuccino"]


    def compare(drink):
        if MENU[drink]["cost"] > resources["Money"]: print("Sorry there is not enough money.")
        if MENU[drink]["ingredients"]["water"] > resources["Water"]: print("Sorry there is not enough water.")
        if MENU[drink]["ingredients"]["milk"] > resources["Milk"]: print("Sorry there is not enough milk.")
        if MENU[drink]["ingredients"]["coffee"] > resources["Coffee"]: print("Sorry there is not enough coffee.")
        return None

    check = compare(choice)
    if check == None: continue




    if choice == "off":
        break

    if choice == "report":
        print("""
        Water: {}ml
        Milk: {}ml
        Coffee: {}g
        Money: ${}
        """.format(resources["Water"], resources["Milk"], resources["Coffee"], resources["Money"]))
