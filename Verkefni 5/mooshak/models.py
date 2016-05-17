from flask import Markup

class Project():
    def __init__(self, pid, name, desc):
        self.name = name
        self.id = pid
        self.desc = desc
        self.users = []
        self.testcases = []

    def add_members(self, people):
        self.users.extend(people)

    def add_testcases(self, cases):
        self.testcases.extend(cases)

    def is_member(self, person):
        return person in self.users

    def render(self):
        return {'id':self.id, 'name':self.name, 'desc': Markup(self.desc) }

