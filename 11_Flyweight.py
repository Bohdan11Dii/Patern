class Car:
    def __init__(self):
        pass

    def cars(self, car_name):
        return "It is ", (car_name)


class Family:
    car_family = {}

    def __new__(cls, name, car_family_id):
        try:
            id  = cls.car_family[car_family_id]
        except KeyError:
            id = object.__new__(cls)
            cls.car_family[car_family_id] = id
        return id
        

    def info_car(self, car_info):
        cg = Car()
        self.car_info = cg.cars(car_info)


    def get_car_info(self):
        return (self.car_info)

car_data = (('a', 1 , 'Audi') , ('a', 2, 'Ferrari'), ('b', 1, 'Audi'))
car_family = []
for i in car_data:
    obj = Family(i[0], i[1])
    obj.info_car(i[2])
    car_family.append(obj)


for i in car_family:
    print("id = " + str(id(i)))
    print(i.get_car_info())