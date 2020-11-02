
class Components:
    def __init__(self, water, milk, coffee_beans, cups, money,):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.money = money


espresso = Components(250, 0, 16, 1, 4)
latte = Components(350, 75, 20, 1, 7)
cappuccino = Components(200, 100, 12, 1, 6)

start_water = 400
start_milk = 540
start_coffee_beans = 120
start_cups = 9
start_money = 550
possible_cups = min([start_water // 250, start_coffee_beans // 16, start_cups // 1])


def check_coffee():
    if possible_cups == start_cups:
        print("Yes, I can make that amount of coffee")
    elif possible_cups > start_cups:
        print(f"Yes, I can make that amount of coffee (and even {possible_cups - start_cups} more than that)")
    else:
        print(f"No, I can make only {possible_cups} cups of coffee")


def print_menu():
    global start_water, start_milk, start_coffee_beans, start_cups, start_money
    print(f"The coffee machine has: \n"
          f"{start_water} of water \n"
          f"{start_milk} of milk \n"
          f"{start_coffee_beans} of coffee beans \n"
          f"{start_cups} of disposable cups \n"
          f"{start_money} of money")


def sorry():

    if start_water < espresso.water or start_water < latte.water or start_water < cappuccino.water:
        print("Sorry, not enough water!")
    elif start_milk < latte.milk or start_water < cappuccino.milk:
        print("Sorry, not enough milk!")
    elif start_coffee_beans < espresso.coffee_beans or start_coffee_beans < latte.coffee_beans or start_coffee_beans < cappuccino.coffee_beans:
        print("Sorry, not enough coffee beans!")
    elif start_cups < 1:
        print("Sorry, not enough cups!")


def buy_coffee():
    global start_water, start_milk, start_coffee_beans, start_cups, start_money
    global espresso, latte, cappuccino

    action = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:, back - to main menu \n")
    while True:
        if action == "1":
            if min([start_water // 250, start_coffee_beans // 16, start_cups // 1]) >= 1:
                print("I have enough resources, making you a coffee!")
                components = espresso
            else:
                sorry()
                break
        elif action == "2":
            if min([start_water // 350, start_milk // 75, start_coffee_beans // 20, start_cups // 1]) >= 1:
                print("I have enough resources, making you a coffee!")
                components = latte
            else:
                sorry()
                break
        elif action == "3":
            if min([start_water // 200, start_milk // 100, start_coffee_beans // 12, start_cups // 1]) >= 1:
                print("I have enough resources, making you a coffee!")
                components = cappuccino
            else:
                print(f"Sorry, no cappuccino :{min([start_water // 200, start_milk // 100, start_coffee_beans // 12, start_cups // 1])}: ")
                break
        if action in "123":
            start_water -= components.water
            start_milk -= components.milk
            start_coffee_beans -= components.coffee_beans
            start_cups -= components.cups
            start_money += components.money
        if action == "back":
            break
        return


def fill_action():
    global start_water, start_milk, start_coffee_beans, start_cups

    water_add = int(input("Write how many ml of water do you want to add:"))
    milk_add = int(input("Write how many ml of milk do you want to add:"))
    coffee_beans_add = int(input("Write how many grams of coffee beans do you want to add:"))
    cups_add = int(input("Write how many disposable cups of coffee do you want to add:"))

    start_water += water_add
    start_milk += milk_add
    start_coffee_beans += coffee_beans_add
    start_cups += cups_add
    return


def take_money():
    global start_money

    print(f"I gave you ${start_money}")
    start_money -= start_money
    return


def start_action():
    while True:
        action = input("Write action (buy, fill, take, remaining, exit): \n")
        if action == "buy":
            buy_coffee()
        elif action == "fill":
            fill_action()
        elif action == "take":
            take_money()
        elif action == "remaining":
            remaining()
        elif action == "exit":
            break


def remaining():
    print_menu()


start_action()
