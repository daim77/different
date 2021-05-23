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


my_fridge = SmartFridge('Bosch', 'ABCx001')
office_fridge = SmartFridge('Miele', 'XYZx999')

bod1 = Points(1, 1)
bod2 = Points(2, 2)
