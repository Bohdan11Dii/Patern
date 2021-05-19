from abc import ABC, abstractmethod
from enum import Enum, auto

class Automachine(Enum):
    disel_car = auto() # дизельна-машина
    electro_car = auto() # електро-машина
    


class Autocharacter(Enum):
    engine = auto()# двигун
    fuel = auto()# паливо
    body_type = auto() # тип кузова


class Autoparts(Enum):
    number_of_doors = auto()# кількість дверей
    icon = auto()# іконка
    color = auto()# колір


class Autotop(Enum):
    model = auto()# модель
    country = auto()# країна виготовлення
    price  = auto()# представник



"""
Клас компонованого продукту
"""

class Auto:
    def __init__(self, name):
        self.name = name
        self.machine = None
        self.character = None
        self.parts = None
        self.topping = None
        self. year = None

    def __str__(self):
        info: str = f"Auto name: {self.name} \n" \
                    f"automachine :{self.machine} \n" \
                    f"autocharacter :{self.character}\n" \
                    f"autoparts : {self.parts}\n" \
                    f"topping : {self.topping}\n" \
                    f"year :{self.year}"
        return info


"""
Абстрактний клас, що задає інтерфейс будівельника
"""

class Builder(ABC):

    @abstractmethod
    def info_machine(self) -> None: pass

    @abstractmethod
    def info_character(self) -> None: pass

    @abstractmethod
    def info_parts(self) -> None: pass

    @abstractmethod
    def info_topping(self) -> None: pass

    @abstractmethod
    def info_auto(self) -> Auto: pass


"""
Реалізація конкретних будівельників для отримання інформації машини
"""


class Volkswagen(Builder):
    def __init__(self):
        self.auto = Auto("Volkswagen")
        self.auto.year = 1999

    def info_machine(self) ->None:
        self.auto.machine = { "Volkswagen" : "disel_car"}

        
    def info_character(self) -> None:
        self.auto.character = {
            "engime" : "1.9","fuel": "disel", "body_type" : "sedan"
        }

    def info_parts(self) -> None:
        self.auto.parts = {
            "number_of_doors" : "4",
            "icon" : "W",
            "color" : "gray"
        }
 
    def info_topping(self) -> None:
        self.auto.topping = {
            "model" : "Passat B5",
            "country" : "Germany",
            "price" :  "$20 000  "
        }
        

    def info_auto(self) -> Auto:
        return self.auto


class Tesla(Builder):
    def __init__(self):
        self.auto = Auto("Tesla")
        self.auto.year = 2020

    def info_machine(self) ->None:
        self.auto.machine = { "Tesla" : "electro_car"}

        
    def info_character(self) -> None:
        self.auto.character = {
            "engime" : "Three electric motors (one in front, two in the back)",
            "fuel": "electrocar", 
            "body_type" : "sedan"
        }

    def info_parts(self) -> None:
        self.auto.parts = {
            "number_of_doors" : "2",
            "icon" : "T",
            "color" : "red"
        }
 
    def info_topping(self) -> None:
        self.auto.topping = {
            "model" : "Tesla Roadster",
            "country" : "American",
            "price" :  "$200,000 "
        }
        

    def info_auto(self) -> Auto:
        return self.auto

"""
Клас Director, відповідаючий за процес машин
"""


class Director:
    def __init__(self):
        self.builder = None


    def set_builder(self, builder: Builder):
        self.builder = builder

    def make_auto(self):
        if not self.builder:
            raise ValueError("Builder didn't set")
        self.builder.info_machine()
        self.builder.info_character()
        self.builder.info_parts()
        self.builder.info_topping()


    
if __name__ == "__main__":
    director = Director() # створюється екземпдяр класа директор
    for it in (Volkswagen,Tesla):
        builder = it() # створюється екземпляр класа 
        director.set_builder(builder)
        director.make_auto()
        auto = builder.info_auto()
        print(auto)
        print('--------------------------------')
        