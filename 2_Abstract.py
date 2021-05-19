class Abstract_factory:
    def create_chair(self):
        raise NotImplementedError()


    def create_sofa(self):
        raise NotImplementedError()

    def create_table(self):
        raise NotImplementedError()


class Modern:
    def __init__(self, name, color, style):
        self.name = name
        self.color = color
        self.style = style

    def __str__(self):
        return "(%s, %s, %s)" % (self.name, self.color, self.style)

class Victorian:
    def __init__(self, name, color, style):
        self.name = name
        self.color = color
        self.style = style

    def __str__(self):
        return "(%s, %s, %s)" % (self.name, self.color, self.style)


class Ar_Deco:
    def __init__(self, name, color, style):
        self.name = name
        self.color = color
        self.style = style

    def __str__(self):
        return "(%s, %s, %s)" % (self.name, self.color, self.style)


class One_product:
    def create_chair(self):
        return Modern("Chair", "White", "Modern")

    def create_sofa(self):
        return Modern("Sofa", "White", "Modern")

    def create_table(self):
        return Modern("Table", "White", "Modern")

class Two_product:
    def create_chair(self):
        return Victorian("Chair", "Gray", "Victorian")

    def create_sofa(self):
        return Victorian("Sofa", "Gray", "Victorian")

    def create_table(self):
        return Victorian("Table", "Gray", "Victorian")

class Three_product:
    def create_chair(self):
        return Ar_Deco("Chair", "Golden", "Ar_Deco")

    def create_sofa(self):
        return Ar_Deco("Sofa", "Golden", "Ar_Deco")

    def create_table(self):
        return Ar_Deco("Table", "Golden", "Ar_Deco")


def get_product(c):
    if c == 1:
        return One_product()
    elif c == 2:
        return Two_product()
    elif c == 3:
        return Three_product()


def menu():
    while True:
        a = input(""""
1 - Modern
2 - Victorian
3 - Ar_Deco
q - exit
Виберіть дію: 
"""  )
        if a == "1":
            product = get_product(1)
            print(product.create_chair(),"\n", product.create_sofa(),"\n", product.create_table())

        elif a == "2":
            product = get_product(2)
            print(product.create_chair(),"\n", product.create_sofa(),"\n", product.create_table())


        elif a == "3":
            product = get_product(3)
            print(product.create_chair(),"\n", product.create_sofa(),"\n", product.create_table())

        elif a == "q":
            break
menu()