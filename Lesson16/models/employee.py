"""Employee"""
from datetime import date, timedelta


class Employee:
    """class Employee"""
    empCount = 0

    def __init__(self, name, surname, mail, salary):
        self.name = name
        self.surname = surname
        self.mail = mail
        self.salary = salary
        Employee.empCount += 1

    @property
    def work(self):
        """work"""
        return "I come to the office."

    def check_salary(self, days=0):
        """check_salary"""
        if not days:
            today = date.today()
            fromdate = date(today.year, today.month, 1)
            daygenerator = (fromdate + timedelta(x) for x in range((today - fromdate).days + 1))
            res = sum(1 for day in daygenerator if day.weekday() < 5)
            return self.salary*res
        return self.salary*days

    def __str__(self):
        return "{}: {} {}".format(self.__class__.__name__, self.name, self.surname)
