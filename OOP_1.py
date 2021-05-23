from datetime import date


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


my_fridge = SmartFridge('Bosch', 'ABCx001')
office_fridge = SmartFridge('Miele', 'XYZx999')
