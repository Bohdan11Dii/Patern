class Dialog:
    def to_print(self, button):
        pass


class Panel(Dialog):
    def to_print(self, button):
        if button == 'Print':
            return 'print to page'

class  Panel_color(Dialog):
    def to_print(self, button):
        if button == 'Red':
            return 'print to page red color'




class Print_:
    def __init__(self):
        self.to_print = []


    def add_to_print(self, p):
        self.to_print.append(p)


    def response(self, button):
        for p in self.to_print:
            pages = p.to_print(button)
            if pages:
                print('Answer', pages)
                break
        else:
            print('No such command found')
            
               
print_in = Print_()
print_in.add_to_print(Panel())
print_in.add_to_print(Panel_color())
print_in.response('Print')
print_in.response('Red')
print_in.response('Save')

















#
#def menu():
#    print_in = Print()
#        
#        
#    a = input('''
#Select a command:
#Print
#Save
#Send\n''')
#    if a == 'Print':
#        print_in.add_to_print(Panel())
#        print_in.response('Print')
#    
#    i = input('''
#Choose a color:
#Red
#White
#Yellow\n''')
#    if i == 'Red':
#        print_in.add_to_print(Panel_color())
#        print_in.response('Red')
#    
#        
#    c = input('Comand:\n')
#    if c == 'Save':
#        print_in.response('404')
#        print('No such command found')
#            
#menu()
#








