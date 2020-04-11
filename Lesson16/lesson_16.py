from datetime import date, timedelta

class Employee:
    empCount = 0

    def __init__(self, name, surname, mail, salary):
        self.name = name
        self.surname = surname
        self.mail = mail
        self.salary = salary
        Employee.empCount += 1

    def work(self):
        return "I come to the office."

    def check_salary(self, days=0):
        if not days:
            today = date.today()
            fromdate = date(today.year, today.month, 1)
            daygenerator = (fromdate + timedelta(x) for x in range((today - fromdate).days + 1))
            res = sum(1 for day in daygenerator if day.weekday() < 5)
            return self.salary*res
        return self.salary*days

    def __str__(self):
        return "{}: {} {}".format(self.__class__.__name__, self.name, self.surname)


class Recruiter(Employee):

    def __init__(self, name, surname, mail, salary):
        super().__init__(name, surname, mail, salary)
        self.hired_this_month = 0

    def work(self):
        empl = super().work()[:-1:]
        return empl + " and start hiring."


class Programmer(Employee):

    def __init__(self, name, surname, mail, salary, tech_stack):
        super().__init__(name, surname, mail, salary)
        self.tech_stack = tech_stack
        self.closed_this_month = []

    def work(self):
        empl = super().work()[:-1:]
        return empl + " and start coding."

    def __add__(self, other):
        return sorted(set(self.tech_stack + other.tech_stack))

    def __gt__(self, other):
        return len(self.tech_stack) > len(other.tech_stack)


recr1 = Recruiter('Ivanna', 'Ivanova', 'recr1@mail.com', 150)
progr1 = Programmer('Ivan', 'Ivanov', 'progr1@mail.com', 250, ['PHP', 'JS', 'MySQL'])
progr2 = Programmer('Petr', 'Petrov', 'progr2@mail.com', 200, ['PHP', 'MySQL', 'C#', '.NET'])
empl1 = Employee('Ivanushka', 'Ivanovich', 'empl1@mail.com', 50)
print(recr1.work())
print(recr1)
print(recr1.check_salary(10))
print(progr1.work())
print(progr1)
print(progr1.check_salary(12))
print(progr2.work())
print(progr2)
print(progr2.check_salary(8))
print(empl1.work())
print(empl1)
print(empl1.check_salary(8))
print(progr1+progr2)
print(not(progr1 > progr2))
print(progr1.check_salary())
