class CoffeeMachine:
    espresso = (250, 0, 16, 1, 4)
    latte = (350, 75, 20, 1, 7)
    cappuccino = (200, 100, 12, 1, 6)
    coffee_types = [espresso, latte, cappuccino]

    def __init__(self, water, milk, coffee_beans, cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.money = money

    def buy_coffee(self):
        action = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if action == "1":
            self.check_coffee(int(action))
        elif action == "2":
            self.check_coffee(int(action))
        elif action == "3":
            self.check_coffee(int(action))
        elif action == "back":
            return

    def check_coffee(self, action):
        if (self.water - self.coffee_types[action - 1][0]) < 0:
            print("Sorry, not enough water!")
            return
        if (self.milk - self.coffee_types[action - 1][1]) < 0:
            print("Sorry, not enough milk!")
            return
        if (self.coffee_beans - self.coffee_types[action - 1][2]) < 0:
            print("Sorry, not enough coffee beans!")
            return
        if self.cups < 1:
            print("Sorry, not enough disposable cups!")
            return
        print("I have enough resources, making you a coffee!")
        self.water -= self.coffee_types[action - 1][0]
        self.milk -= self.coffee_types[action - 1][1]
        self.coffee_beans -= self.coffee_types[action - 1][2]
        self.cups -= 1
        self.money += self.coffee_types[action - 1][4]

    def print_menu(self):

        print(f"The coffee machine has: \n"
              f"{self.water} of water \n"
              f"{self.milk} of milk \n"
              f"{self.coffee_beans} of coffee beans \n"
              f"{self.cups} of disposable cups \n"
              f"{self.money} of money")

    def fill_action(self):

        water_add = int(input("Write how many ml of water do you want to add:\n"))
        milk_add = int(input("Write how many ml of milk do you want to add:\n"))
        coffee_beans_add = int(input("Write how many grams of coffee beans do you want to add:\n"))
        cups_add = int(input("Write how many disposable cups of coffee do you want to add:\n"))

        self.water += water_add
        self.milk += milk_add
        self.coffee_beans += coffee_beans_add
        self.cups += cups_add

    def take_money(self):
        print(f"I gave you ${self.money}")
        self.money -= self.money

    def remaining(self):
        self.print_menu()

    def do_action(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit):\n")
            if action == "buy":
                self.buy_coffee()
            elif action == "fill":
                self.fill_action()
            elif action == "take":
                self.take_money()
            elif action == "remaining":
                self.remaining()
            elif action == "exit":
                break


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
coffee_machine.do_action()
