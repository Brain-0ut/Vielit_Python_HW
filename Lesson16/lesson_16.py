"""Main module"""
from Lesson16.models.position import *

recr1 = Recruiter('Ivanna', 'Ivanova', 'recr1@mail.com', 150)
progr1 = Programmer('Ivan', 'Ivanov', 'progr1@mail.com', 250, ['PHP', 'JS', 'MySQL'])
progr2 = Programmer('Petr', 'Petrov', 'progr2@mail.com', 200, ['PHP', 'MySQL', 'C#', '.NET'])
empl1 = Employee('Ivanushka', 'Ivanovich', 'empl1@mail.com', 50)
cand1 = Candidate("Ibrahim Suleyman", ['python', 'JS', 'PHP'], 'python', 'strong middle')
recr1.salary = 120
progr1.mail = 'progr11@mail.com'
progr2.tech_stack += ['python']
empl1.salary = 60
cand1.main_skill_level = 'middle'
print(recr1.work())
print(recr1)
print(recr1.check_salary(10))
print(progr1.work())
print(progr1)
print(progr1.check_salary(12))
print(progr2.work())
print(progr2)
print(progr2.check_salary(8))
print(empl1.work)
print(empl1)
print(empl1.check_salary(8))
print(progr1+progr2)
print(not(progr1 > progr2))
print(progr1.check_salary())
