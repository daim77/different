class SmartFridge:

    def __init__(self, brand, serial_number):
        self.brand = brand
        self.serial_number = serial_number

    def greet(self):
        print(f'Hello! I am {self.brand}')


my_fridge = SmartFridge('Bosch', 'ABCx001')
office_fridge = SmartFridge('Miele', 'XYZx999')




