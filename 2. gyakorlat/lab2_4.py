class StringPrinter:

    #my_string = 'Default string'

    def __init__(self, my_str = 'Default string'):
        self.my_string = my_str

    def set_string(self):
        self.my_string = input('Kerek egy uj stringet: ')

    def print_string(self):
        print(self.my_string.upper())


my_str = StringPrinter()
print(my_str.my_string)
my_str.set_string()
my_str.print_string()
