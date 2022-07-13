fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.


def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit + " pie")
    except IndexError as error_message:
        print(f"The {error_message} does not exist!")
    else:
        print("The ingredient added!")


make_pie(2)