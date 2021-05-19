class Client:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print('Доброго дня,', self.name)
        return self.name

    

class Shop:
    def product(self):
        while True:
        
            product = input( 'Що бажаєте замовити? ')
            print("Перевіряємо - ", product)
            if product == 'Машину'.lower() or product == 'Телефон'.lower() or product == 'Квартиру'.lower():
                print(product,"Є в наявності. Даєте дозвіл на пакування продукту?" )
                a = input()
                if a == 'Так'.lower():
                    print("Добре, ваш продукт пішов на пакування") 
                    print('Ваш продукт прибуде завтра в 11:00 київського часу')
                    break
                elif a == "Ні".lower():
                    print('Виберіть інший продукт')
                    continue
            else:
                print('Вибачте, але цього предмету немає в наявності. Можу запропонувати машину, телефон або квартиру')
          
            continue
            

        

    
        
        

    def payment_system(self):
        while True:
            a = input("Виберіть  систему оплати: 1 - готівка, 2 - картка\n")
            if a == '1':
                print("Добре, ваша  система оплати - готівка")
            elif a == '2':
                print("Добре, ваша  система оплати - картка")
            else:
                print("Ви вибрали непідтримувану операцію")
                continue
            print('Дякуємо, що обрали нашу мережу')
            break


class Facade:
    def __init__(self):
        self.shop = Shop()
        self.client = Client("Bohdan")

    def spoke(self):
        self.client.get_name()
        self.shop.product()
        self.shop.payment_system()

f = Facade()
f.spoke()