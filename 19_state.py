class telephone_function:
    

    def get_button(self):
        pass
        


class  unlocked(telephone_function):
    def get_button(self):
        return 'Open Google'

class blocked(telephone_function):
    def get_button(self):
        return 'Unlocked telephone'


class discharged(telephone_function):
    def get_button(self):
        return 'Phone status 5%'


class telephone:
    def __init__(self):
        self.current_sate = None
        self.state = self.get_state()

    def get_state(self):
        return [unlocked(), blocked(), discharged()]

    def next_state(self):
        if self.current_sate is None:
            self.current_sate = self.state[0]
        else:
            index = self.state.index(self.current_sate)
            if index < len(self.state) - 1:
                index += 1
            else:
                index = 0
            self.current_sate = self.state[index]
        return self.current_sate


    def function(self):
        state = self.next_state()
        print(state.get_button())

t = telephone()
[t.function() for i in range(3)]

