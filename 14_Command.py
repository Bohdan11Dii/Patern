class Client:
    def sent_the_order(self):
        print("Зробити замовлення")


    def received_an_order(self):
        print("Отримати замовлення")


class Waiter:
    def order(self):
        pass

class Client_and_Waiter(Waiter):
    def __init__(self, client):
        self.client = client


class Sent_The_Order(Client_and_Waiter):
    def order(self):
        self.client.sent_the_order()

class Received_An_Order(Client_and_Waiter):
    def order(self):
        self.client.received_an_order()


class Cook:
    def __init__(self, sto_cmd, rao_cmd):
        self.sto_cmd = sto_cmd
        self.rao_cmd = rao_cmd

    def sto(self):
        self.sto_cmd.order()


    def rao(self):
        self.rao_cmd.order()

client = Client()

cook = Cook(sto_cmd = Sent_The_Order(client), rao_cmd = Received_An_Order(client))
cook.sto()
cook.rao()