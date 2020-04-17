"""Main module"""
from Lesson16.models.position import *
from Lesson16.models.vacancy import Vacancy

if __name__ == '__main__':
    recr_1 = Recruiter('Ivanna', 'Ivanova', 'recr1@mail.com', 150)
    progr_1 = Programmer('Ivan', 'Ivanov', 'progr1@mail.com', 250, ['PHP', 'JS', 'MySQL'])
    progr_2 = Programmer('Petr', 'Petrov', 'progr2@mail.com', 200, ['PHP', 'MySQL', 'C#', '.NET'])
    empl_1 = Employee('Ivanushka', 'Ivanovich', 'empl1@mail.com', 50)
    cand_1 = Candidate("Ibrahim Suleyman", ['python', 'JS', 'PHP'], 'python', 'strong middle')
    cand_2 = Candidate("Jora Pichen`kin", ['JS', 'PHP', 'Assembler'], 'JS', 'middle')
    cand_3 = Candidate("Ibrahim Suleyman", ['JS', 'PHP', 'MySQL'], 'PHP', 'junior')
    vacancy_1 = Vacancy('Python programmer for new project', 'python', 'junior')
    vacancy_2 = Vacancy('Python programmer for new project', 'python', 'middle')
    recr_1.salary = 120
    progr_1.mail = 'progr11@mail.com'
    progr_2.tech_stack += ['python']
    empl_1.salary = 60
    cand_1.main_skill_level = 'middle'
    print(recr_1.work())
    print(recr_1)
    print(recr_1.check_salary(10))
    print(progr_1.work())
    print(progr_1)
    print(progr_1.check_salary(12))
    print(progr_2.work())
    print(progr_2)
    print(progr_2.check_salary(8))
    print(empl_1.work)
    print(empl_1)
    print(empl_1.check_salary(8))
    print(progr_1 + progr_2)
    print(not (progr_1 > progr_2))
    print(progr_1.check_salary())
    print(vacancy_1.__dict__)
