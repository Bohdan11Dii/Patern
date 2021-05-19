class Duck(object):
    def __init__(self, name):
        self._name = name

    def say(self):
        print("Привіт, мене звати %s" % self._name)


class Wings(object):
    def __init__(self, duck):
        self._duck = duck

    def __getattr__(self, item):
        return getattr(self._duck, item)


    def fly(self):
        print("%s полетів у теплі краї" % self._duck._name)


class Swim(object):
    def __init__(self, duck):
        self._duck = duck

    def __getattr__(self, item):
        return getattr(self._duck, item)

    def swim(self):
        print("%s плаває зі своїми друзями" % self._duck._name )



def menu():
    duck = Duck(input("Ввести імя обєкта: \n"))
    while True:
        
        c = input("Виберіть операцію: 1 - літати , 2 - плавати, 3 - повна інформація\n ")

        if c == '1':
            duck_wings = Wings(duck)
            duck_wings.say()
            duck_wings.fly()
        elif c == '2':
            duck_swim = Swim(duck)
            duck_swim.say()
            duck_swim.swim()

        elif c == '3':
            duck_wings = Wings(duck)
            duck_wings.say()
            duck_wings.fly()
            duck_swim = Swim(duck)
            duck_swim.swim()
        else:
            break
menu()