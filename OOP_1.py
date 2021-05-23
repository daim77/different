from datetime import date


# info about fridge
class SmartFridge:

    fridge_counter = 0

    def __init__(self, brand, serial_number):
        self.brand = brand
        self.serial_number = serial_number
        self.f_date = date.today()  # factory date
        SmartFridge.fridge_counter += 1

    def greet(self):
        print(f'Hello! I am {self.brand}')

    def age(self):
        print(
            f'Fridge {self.brand} '
            f'serial number {self.serial_number} '
            f'is {(date.today() - self.f_date).days} days old'
        )


# Two points and distance
class Points:
    counter = 0

    def __init__(self, x, y):
        self.x_value = x
        self.y_value = y
        Points.counter += 1

    def distance(self, point2):
        print(
            f'Distance between '
            f'{self} and '
            f'{point2} is '
            f'{((self.x_value - point2.x_value) ** 2 + (self.y_value - point2.y_value) ** 2) ** (1/2)}'
        )


# phone
class Phone:
    counter = 0

    def __init__(self, brand: str, sn: str):
        self.brand = brand
        self.serial_number = sn
        self.contact_dict = dict()
        Phone.counter += 1

    def add_contact(self, surname: str, name: str, phone_number: str):
        if surname + ' ' + name in self.contact_dict:
            print(f'{surname}, {name} contact is already in the list')
            what_to_do = \
                input('press 0 to skip action or 1 to overwrite contact')
            if what_to_do == '0':
                return
            elif what_to_do == '1':
                self.contact_dict.update({surname + ' ' + name: phone_number})
                print(f'contact {surname}, {name}, {phone_number} saved')
        self.contact_dict.update({surname + ' ' + name: phone_number})
        print(f'contact {surname}, {name}, {phone_number} saved')

    def del_contact(self, surname: str, name: str):
        if self.contact_dict.pop(surname + ' ' + name, 'deleted') == 'deleted':
            print(f'Contact {surname}, {name} not in the list')

    def search_contact(self):
        for key in self.contact_dict:
            print(key, ':', self.contact_dict[key])


iphone = Phone('iPhone', 'sn0001')

my_fridge = SmartFridge('Bosch', 'ABCx001')
office_fridge = SmartFridge('Miele', 'XYZx999')

bod1 = Points(1, 1)
bod2 = Points(2, 2)
