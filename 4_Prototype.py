import copy 

class Auto:
    def __init__(self, name, age, model):
        self.name = name
        self.age = age
        self.model = model

    def __str__(self):
        return "{}, {}, {}".format(self.name, self.age, self.model)



    
    def main(self):
        auto = Auto(self.name, self.age, self.model)
        auto_copy = copy.deepcopy(auto)
        print(auto_copy)


a = Auto('Volkswagen', '1999', 'Pasat B5')
a.main()
