class creator:
    def __init__(self):
        self.data = None
        self.observers = set()


    def attach(self, observer):
        if not isinstance(observer, Observer_base):
            raise TypeError()

        self.observers.add(observer)

    def detach(self, observer):
        self.observers.remove(observer)


    def get_data(self):
        return self.data


    def set_data(self, data):
        self.data = data
        self.notify(data)

    def notify(self,data):
        for observer in self.observers:
            observer.updata(data)


class Observer_base:
    def updata(self, data):
        pass


class Observer(Observer_base):
    def __init__(self,name):
        self.name = name


    def updata(self, data):
        print('%s: %s' % (self.name, data))



cr = creator()
cr.attach(Observer('Перший підписник'))
cr.attach(Observer('Другий підписник'))
cr.set_data('приєднався 10.04.1999')


