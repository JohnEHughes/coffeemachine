import sys

class CoffeeMachine:

    def __init__(self, water, milk, coffee_beans, cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.money = money


    def status(self):
        print()
        print("The coffee machine has:")
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.coffee_beans} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'${self.money} of money')
        print()



    def espresso(self):
        print("I have enough resources, making you a coffee!")
        # global money, water, coffee_beans, cups
        self.money += 4
        self.water -= 250
        self.coffee_beans -= 16
        self.cups -=1
        print()
        self.welcome()


    def latte(self):
        print("I have enough resources, making you a coffee!")
        # global money, water, coffee_beans, cups, milk
        self.money += 7
        self.water -= 350
        self.coffee_beans -= 20
        self.milk -= 75
        self.cups -= 1
        print()
        self.welcome()


    def cappuccino(self):
        print("I have enough resources, making you a coffee!")
        # global money, water, coffee_beans, cups, milk
        self.money += 6
        self.water -= 200
        self.coffee_beans -= 12
        self.milk -= 100
        self.cups -= 1
        print()
        self.welcome()


    def fill(self):
        # global money, water, coffee_beans, cups, milk
        print()
        add_water = int(input("Write how many ml of water do you want to add: "))
        add_milk = int(input("Write how many ml of milk do you want to add: "))
        add_coffee = int(input("Write how many grams of coffee beans do you want to add: "))
        add_cups = int(input("Write how many disposable cups do you want to add: "))
        self.water += add_water
        self.milk += add_milk
        self.coffee_beans += add_coffee
        self.cups += add_cups
        # status()

        self.welcome()

    def buy(self):
        print()
        to_buy = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        if to_buy == "1":
            if self.water >= 250 and self.coffee_beans >= 16 and self.cups >= 1:
                self.espresso()
            elif self.water < 250:
                print("Sorry, not enough water")
            elif self.coffee_beans < 16:
                print("Sorry, not enough coffee beans")
            elif self.cups < 1:
                print("Sorry, not enough disposable cups")
        elif to_buy == "2":
            if self.water >= 350 and self.coffee_beans >= 20 and self.milk >= 75 and self.cups >= 1:
                self.latte()
            elif self.water < 350:
                print("Sorry, not enough water")
            elif self.coffee_beans < 20:
                print("Sorry, not enough coffee beans")
            elif self.milk < 75:
                print("Sorry, not enough milk")
            elif self.cups < 1:
                print("Sorry, not enough disposable cups")
        elif to_buy == "3":
            if self.water >= 200 and self.coffee_beans >= 12 and self.milk >= 100 and self.cups >= 1:
                self.cappuccino()
            elif self.water < 200:
                print("Sorry, not enough water")
            elif self.coffee_beans < 12:
                print("Sorry, not enough coffee beans")
            elif self.milk < 100:
                print("Sorry, not enough milk")
            elif self.cups < 1:
                print("Sorry, not enough disposable cups")
        elif to_buy == "back":

            self.welcome()

        print()
        self.welcome()
        # else:
        #     welcome()


    def take(self):
        # global money
        print(f'I gave you ${self.money}')
        self.money = 0
        # status()
        self.welcome()


    def welcome(self):
        # status()
        print()
        action = input("Write action (buy, fill, take, remaining, exit): ")
        if action == "buy":
            self.buy()
        elif action == "fill":
            self.fill()
        elif action == "take":
            self.take()
        elif action == "exit":
            sys.exit()
        elif action == "remaining":
            self.status()
            self.welcome()


machine1 = CoffeeMachine(400, 540, 120, 9, 550)
machine1.welcome()






