class sales_shop:

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

        dic = {"Ice_cream": [ju.qty_ss, ju.qty_ms],
               "Meat_pie": [mit.qty_ss, mit.qty_ms],
               "Juice": [ice.qty_ss, ice.qty_ms]
               }
        if prod == "all":
            for keys, values in dic.items():
                print("{} remains: Small size {}, Medium size {}".format(keys, values[0], values[1]))
        for keys, values in dic.items():
            if prod == keys:
                for i in range(len(values)):
                    while i == 0:
                        print("Small-size remains {}.".format(values[0]))
                        break
                    while i == 1:
                        print("Medium-size remains {}.".format(values[1]))
                        break
b = sales_shop()
b.Querry("Juice")