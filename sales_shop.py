import os
import sys
class sales_shop:
    lis = ["Meat_pie", "Juice", "Ice_cream"]
    option = ["Query"]
    def __int__(self):
        self.ss = ""
        self.ms = ""
        self.qty_ms = ""
        self.qty_ss = ""

    def Ice_cream(self):
        self.ss = 500
        self.ms = 1500
        self.qty_ss = 24
        self.qty_ms = 52

    def Meat_pie(self):
        self.ss = 250
        self.ms = 420
        self.qty_ss = 380
        self.qty_ms = 420

    def Juice(self):
        self.ss = 850
        self.ms = 1250
        self.qty_ss = 530
        self.qty_ms = 578

    def Querry(self, prod):
        ju = sales_shop()
        ju.Juice()
        mit = sales_shop()
        mit.Meat_pie()
        ice = sales_shop()
        ice.Ice_cream()

        dic = {"Ice_cream": [ice.qty_ss, ice.qty_ms],
               "Meat_pie": [mit.qty_ss, mit.qty_ms],
               "Juice": [ju.qty_ss, ju.qty_ms]
               }

        if prod == "All":
            for keys, values in dic.items():
                print("{} remains: Small size {}, Medium size {}".format(keys, values[0], values[1]))
        elif not prod or prod not in dic:
            print("Invalid Querry option")
        else:
            for keys, values in dic.items():
                if prod == keys:
                    for i in range(len(values)):
                        while i == 0:
                            print("Small-size remains {}.".format(values[0]))
                            break
                        while i == 1:
                            print("Medium-size remains {}.".format(values[1]))
                            break


def rem(inp):
    b = sales_shop()
    b.Querry(inp.capitalize())


def check(*args):
    if args[0].capitalize() in sales_shop().option:
        if args[1].capitalize() in sales_shop().lis:
            rem(arg[1])
    else:
        loop(arg[0])


print("1 : Customer\n2 : Seller")
quad = int(input("\nSelect 1 if you are a customer, or 2 if you are a seller\t\t"))
arg = ""
while True:
    if quad == 1 or quad == 2:
        break
    else:
        quad = int(input("Invalid selection, try again: "))

if quad == 1:
    print("to be carried out later. bye for now")
    sys.exit()

elif quad == 2:
    print("\nwelcome, to query, please key in the command Query with the product\ne.g Query Juice\n")
    command = input("Command$ ")
    arg = command.split(" ")
    check(arg[0], arg[1])


def loop(valid):
    while True:
        if valid.capitalize() not in sales_shop().option:
            print("Invalid Product, try again:")
            law = input("Command$ ")
            


    else:
        print("Invalid Command, try again:")
        command = input("Command$ ")