class House:
    def __init__(self, name):
        self.name = name
        print("Hello", name)


    def order(self):
        self.pouring_the_foundation()
        self.pulling_walls()
        self.roofing()
        self.installation_of_windows_and_doors()


    def pouring_the_foundation(self):
        pass

    def pulling_walls(self):
        pass
    

    def roofing(self):
        pass


    def installation_of_windows_and_doors(self):
        pass

class Realization(House):
    def pouring_the_foundation(self):
        print("Перший крок заливаємо фундамент")
        
    def pulling_walls(self):
        print("Другий крок протягуєм стіни")
    

    def roofing(self):
        print("Третій крок покриття даху")


    def installation_of_windows_and_doors(self):
        print("Четвертий крок встановлення вікон та дверей")



real = Realization('Bohdan')
real.order()