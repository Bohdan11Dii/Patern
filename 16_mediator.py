class Pilots:
    def coordinates(self):
        pass

    def landing_place(self):
        pass


class Helicopter(Pilots):
    def coordinates(self):
        print("Helicopter: my coordinates - 41.40338, 2.17403")


    def landing_place(self):
        print("Landing airoport in London")



class Plane(Pilots):
    def coordinates(self):
        print("Plane: my coordinates - 51.21338, 3.14133")


    def landing_place(self):
        print("Landing airoport in USA")


class Dispatcher:
    def __init__(self):
        self.pilots = ['coordinates' , 'landing_place']

    def coordinates(self, show):
        show.landing_place()
        show.coordinates()

    def set_coordinates(self, show):
        self.pilots['coordinates'] = show

    def set_landing_plasce(self, show):
        self.pilots['landing_place'] = show


helicopter_show = Helicopter()
plane_show = Plane()

dispatcher = Dispatcher()
dispatcher.coordinates(helicopter_show)
dispatcher.coordinates(plane_show)




