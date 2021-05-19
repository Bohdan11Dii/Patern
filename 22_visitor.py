class Zoo_visitor(object):
    def look(self, zoo):
        
        animals = {
            Leo: self.look_leo,
            Tiger: self.look_tiger,
            Snake: self.look_snake,
            Shark: self.look_shark

        }
        look = animals.get(type(zoo), self.look_unknown)
        look(zoo)

    
    
    def look_leo(self, zoo):
        print("Лев\n", zoo.name, zoo.age)
    def look_tiger(self, zoo):
        print("Тигр\n" , zoo.name, zoo.age)
    def look_snake(self, zoo):
        print("Змія\n", zoo.name, zoo.age)
    def look_shark(self, zoo):
        print("Акула\n", zoo.name, zoo.age)
    def look_unknown(self, zoo):
        print("Тварина\n", zoo.name, zoo.age)



class Zoo_animal(object):
    def look(self, visitor):
        visitor.look(self)

    def __init__(self, name, age):
        self.name = name
        self.age = age



class Leo(Zoo_animal):
    pass

class Tiger(Zoo_animal):
   pass


class Snake(Zoo_animal):
    pass


class Shark(Zoo_animal):
    pass

class Hodzila(Zoo_animal):
    pass




visitor = Zoo_visitor()

leo = Leo('Сімба', 12)
leo.look(visitor)


tiger = Tiger('Шерхан', 20)
tiger.look(visitor)


snake = Snake('Аджа', 22)
snake.look(visitor)

shark = Shark('Мег', 30)
shark.look(visitor)

hodzila = Hodzila('_', '-_-')
hodzila.look(visitor)