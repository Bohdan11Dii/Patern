class memento:
    def __init__(self, name):
        self.name = name


    def get_save_name(self):
        return self.name


class origin:

    name = ''
    def set(self, name):
        print("Origin - ", name)


    def save_to_memento(self):
        print("Origin, save to memento")
        return memento(self.name)


    def restore_from_memento(self, memento_):
        self.name = memento_.get_save_name()
        print("Origin, state after restoring from memento ", self.name)

save_name = []

or_ = origin()
or_.set("state_1")
or_.set("state_2")


save_name.append(or_.save_to_memento())

or_.set('state_3')
save_name.append(or_.save_to_memento())


or_.set('state_4')
or_.restore_from_memento(save_name[0])
