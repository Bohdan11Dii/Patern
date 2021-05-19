class Payment:
    def penny(self):
        print("Оплата ")

 
class card:
    def __init__(self):
        self.payment = Payment()

    def penny(self):
        
        self.payment.penny()

c = card()
c.penny()



