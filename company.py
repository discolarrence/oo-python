class Employee:
    num_of_employees = 0
    raise_amt = 1.04  

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise(cls, amount):
        cls.raise_amt = amount
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

        


emp_1 = Employee('Laura', 'Rountree', 55000)
emp_2 = Employee('Liam', 'Bushaw', 60000)

import datetime
my_date = datetime.date(2021, 5, 29)

print(Employee.is_workday(my_date))

# emp_str_1 = 'Michelle-Harrington-70000'
# emp_str_2 = 'Taiisha-Devonish-75000'
# emp_str_3 = 'Tracey-Turnblad-65000'

# new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.email)
# print(new_emp_1.pay)

# print(emp_1.fullname())
# print(Employee.fullname(emp_1))

# Employee.set_raise_amt(1.05)

# print(emp_1.raise_amt)
# print(Employee.raise_amt)

# print(emp_1.__dict__)
# print(Employee.__dict__)

# print(Employee.num_of_employees)