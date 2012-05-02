# -*- coding: utf-8 -*-
import inspect

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

#    def giveRaise(self, percent):
#        self.pay = int(self.pay * (1 + percent))
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percens))
    def __str__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)
    def olololololo(self):
        print "OLOLOLOL"

class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus=100):
        Person.giveRaise(self, percent + bonus)