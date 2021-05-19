class Document:
    def __init__(self):
        print("У наявності є два документи")

    
    
    

class pdf(Document):
    def show(self):
        print("Відкрити pdf документ")


class exel(Document):
    def show(self):
        print("Відкрити exel документи")


class Factory:
    def choice(self, type_):
        if type_ == 'pdf':
            return pdf()

        elif type_ == 'exel':
            return exel()



factory = Factory()
factory.choice('pdf').show()
print()
factory.choice('exel').show()



















#def menu():
#    while True:
#        factory = Factory()
#        i = input('Виберіть формат документу : 1 - pdf, 2 - exel, q - вихід\n')
#        if i == '1':
#            factory.choice('pdf').show()
#        elif i == '2':
#            factory.choice('exel').show()
#        elif i == 'q':
#            break
#
#menu()


