class Box:
    def name(self, name):
        raise NotImplementedError

    def function(self):
        raise NotImplementedError

    def price(self):
        raise NotImplementedError


class hummer(Box):
    def name(self):
        print("Назва - Молоток")

    def function(self):
        print("Його суть полягає в забиванні цвяхів в дошку")

    def price(self):
        print("Його ціна - $20")


class telephone(Box):
    def name(self):
        print("Назва Телефон")

    def function(self):
        print("Його основна задача полягеє в спілкуванні на відстані")

    def price(self):
        print("Його ціна становить - $200")


class charging (Box):
    def name(self):
        print("Назва - Зарядне")

    def function(self):
        print("Його основна задача полягеє в зарядці пристроїв")

    def price(self):
        print("Приблизна ціна становить на ринку - $50")


class Information(Box):
    def __init__(self):
        self.items = []


    def name(self):
        print("Предмети які лежать у коробці: ")
        for obj in self.items:
            obj.name()


    def add(self, obj):
        if isinstance(obj, Box) and not obj in self.items:
            self.items.append(obj)


    def get_item(self, index):
        return self.items[index]

info = Information()
info.add(hummer())
info.add(telephone())
info.add(charging())
info.name()



def menu():
    while True:
        a = input("""
1 - Молоток
2 - Телефон
3 - Зарядка
q - вихід
Виберіть потрібний предмет: 
      """)
        if a == "1":
            item = info.get_item(0)
            item.name()
            item.function()
            item.price()

        elif a == "2":
            item = info.get_item(1)
            item.name()
            item.function()
            item.price()

        elif a == "3":
            item = info.get_item(2)
            item.name()
            item.function()
            item.price()

        elif a == "q":
            break
menu()