class Englishman:
    def speak_english(self):
        print('Hello, I am for England')




class Frenchman:
    def speak_french(self):
        print('Salut, je suis pour la France')



class Translate:
    def __init__(self, translate):
        self.translate = translate


    def connect(self):
        self.translate.speak_english()

class Adapter:
    def __init__(self):
        self.french_man = Frenchman()



    def speak_english(self):
        self.french_man.speak_french()


en = Englishman()
tr = Translate(en)
tr.connect()


ad = Adapter()
tr = Translate(ad)
tr.connect()