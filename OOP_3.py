from datetime import date


class Person:

    def __init__(self, name, sex, address, nationality, birthdate):
        self.name = name
        self.sex = sex
        self.address = address
        self.nationality = nationality
        self.birthdate = birthdate

    def calculate_age(self):
        return round((date.today() - self.birthdate).days / 365, 2)


class Trainee(Person):
    vacation_base = 20

    def __init__(self, name, sex, address, nationality, birthday, id,
                 department, performance=None):

        super().__init__(name, sex, address, nationality, birthday)

        self.id = id
        self.department = department
        self.performance = performance

    @property
    def get_vacation(self):
        if self.performance:
            return self.performance / 100 * Trainee.vacation_base
        else:
            raise AttributeError ('set performance first')


class Employee(Person):
    def __init__(self, name, sex, address, nationality,
                 birthdate, id_num, department, salary):

        super().__init__(name, sex, address, nationality, birthdate)

        self.id_num = id_num
        self.department = department
        self.performance = None
        self.salary = salary

    def calculate_age(self):
        diff = date.today() - self.birthdate
        return round(diff.days // 365)


class Manager(Employee):
    pass


class Programmer(Employee):
    def __init__(self, name, sex, address, nationality,
                 birthdate, id_num, department, salary, level):

        super().__init__(name, sex, address, nationality, birthdate,
                         id_num, department, salary)

        self.level = level
        self.age = super(Employee, self).calculate_age()

    def change_address(self, new_address):
        self.address = new_address
        return self.address


class HRAdmin(Employee):
    pass


if __name__ == '__main__':
    Martin = Programmer('martin', 'male', 'Na Luka', 'CZE', date(1977, 6, 10),
                        '007', 'Euromedia', 50000, 'junior')
    print(Martin.age)

    tom = Trainee('Tom', 'male', 'home', 'SK', date(1980, 10, 10),
                  '10', 'IT')
    print(tom.get_vacation())
