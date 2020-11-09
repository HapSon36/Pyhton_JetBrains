class CoffeeMachine:
    espresso = [250, 0, 16, 1, 4]
    latte = [350, 75, 20, 1, 7]
    cappuccino = [200, 100, 12, 1, 6]

    def __init__(self, water, milk, coffee_beans, cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.money = money

    def print_menu(self):
        print(f"The coffee machine has: \n"
              f"{self.water} of water \n"
              f"{self.milk} of milk \n"
              f"{self.coffee_beans} of coffee beans \n"
              f"{self.cups} of disposable cups \n"
              f"{self.money} of money")

    def buy_coffee(self):
        action = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if action == "1":
            if self.water - self.espresso[0] < 0:
                print("Sorry, not enough water!")
            elif self.milk - self.espresso[1] < 0:
                print("Sorry, not enough milk!")
            elif self.coffee_beans - self.espresso[2] < 0:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 0:
                print("Sorry, not enough disposable cups!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= self.espresso[0]
                self.milk -= self.espresso[1]
                self.coffee_beans -= self.espresso[2]
                self.cups -= self.espresso[3]
                self.money += self.espresso[4]
        elif action == "2":
            if self.water - self.latte[0] < 0:
                print("Sorry, not enough water!")
            elif self.milk - self.latte[1] < 0:
                print("Sorry, not enough milk!")
            elif self.coffee_beans - self.latte[2] < 0:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 0:
                print("Sorry, not enough disposable cups!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= self.latte[0]
                self.milk -= self.latte[1]
                self.coffee_beans -= self.latte[2]
                self.cups -= self.latte[3]
                self.money += self.latte[4]
        elif action == "3":
            if self.water - self.cappuccino[0] < 0:
                print("Sorry, not enough water!")
            elif self.milk - self.cappuccino[1] < 0:
                print("Sorry, not enough milk!")
            elif self.coffee_beans - self.cappuccino[2] < 0:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 0:
                print("Sorry, not enough disposable cups!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= self.cappuccino[0]
                self.milk -= self.cappuccino[1]
                self.coffee_beans -= self.cappuccino[2]
                self.cups -= self.cappuccino[3]
                self.money += self.cappuccino[4]
        elif action == "back":
            return

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

    def doaction(self):
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
coffee_machine.doaction()