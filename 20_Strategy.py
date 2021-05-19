class Transport:
    def __init__(self):
        pass



class bicycle(Transport):
    def __init__(self):
        print("We ride a bike, 30 minutes on the road")


class taxi(Transport):
    def __init__(self):
        print("Let's take a taxi, 10 minutes on the road")



class bus(Transport):
    def __init__(self):
        print("we will go by bus, we will be on the road for 20 minutes")


class Aeroport:
    def transport (self):
        s = input("How much money do you have?: 0$, 20$, 50% ")
        if s == "0":
            print("You better ride a bike")
            return bicycle()

        elif s == "20$":
            print("You can go by bus")
            return bus()

        elif s == "50$":
            print("Oh great, you can safely take a taxi")
            return taxi()





a = Aeroport()
a.transport()

