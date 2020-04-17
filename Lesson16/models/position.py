"""Positions"""
from Lesson16.models.employee import *


class Candidate:
    """class Candidate"""

    def __init__(self, full_name, skills, main_skill, main_skill_level):
        self.full_name = full_name
        self.skills = skills
        self.main_skill = main_skill
        self.main_skill_level = main_skill_level


class Recruiter(Employee):
    """class Recruiter(Employee)"""

    def __init__(self, name, surname, mail, salary):
        super().__init__(name, surname, mail, salary)
        self.hired_this_month = 0

    def work(self):
        """work"""
        empl = super().work[:-1:]
        return empl + " and start hiring."


class Programmer(Employee):
    """class Programmer(Employee)"""

    def __init__(self, name, surname, mail, salary, tech_stack):
        super().__init__(name, surname, mail, salary)
        self.tech_stack = tech_stack
        self.closed_this_month = []

    def work(self):
        """work"""
        empl = super().work[:-1:]
        return empl + " and start coding."

    def __add__(self, other):
        return sorted(set(self.tech_stack + other.tech_stack))

    def __gt__(self, other):
        return len(self.tech_stack) > len(other.tech_stack)
