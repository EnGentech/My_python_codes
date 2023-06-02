import os
import sys
class sales_shop:
    lis = ["Meat_pie", "Juice", "Ice_cream", "All"]
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
            print("Invalid Query option")
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
        if len(args) > 1:
            if args[1].capitalize() in sales_shop().lis:
                rem(args[1])
            else:
                loop_product(args[1])
        else:
            print("No product selected")
            new = input("Command$ ")
            new = new.split()
            if len(new) > 1:
                check(new[0], new[1])
            else:
                check(new[0])
    else:
        loop(arg[0])


def loop(valid):
    if valid.capitalize() not in sales_shop().option:
        print("Invalid Command, try again:")
        new = input("Command$ ")
        new = new.split()
        if len(new) > 1:
            check(new[0], new[1])
        else:
            check(new[0])


def loop_product(prd):
    if prd.capitalize() not in sales_shop().lis:
        print("Invalid Product, try again:")
        new = input("Command$ ")
        new = new.split()
        if len(new) > 1:
            check(new[0], new[1])
        else:
            check(new[0])


print("\n========== Welcome to your Service assistance ==========")
print("Select 1 if you are a customer, or 2 if you are a seller\t")
quad = input("Command$ ")

while True:
    if quad == "1":
        print("To be carried out later. bye for now")
        sys.exit()

    elif quad == "2":
        print("\nTo query, please key in the command Query with the product\ne.g Query Juice\n")
        command = input("Command$ ")
        arg = command.split(" ")
        if len(arg) > 1:
            check(arg[0], arg[1])
        else:
            check(arg[0])
    else:
        quad = input("Invalid selection, try again: ")