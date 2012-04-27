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
    def giveRaise(self, percens):
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


b = Person("Bob", "dev", 1000)
print "DIR Person", dir(b)

a = Manager("Bob", 2000)
#print "DIR Manager", dir(a)

#print a.__dict__

print "DICT Person = " , Person.__dict__
#print "Module Person  = " , Person.__module__
#print "CLASS Person = " , Person.__class__
#print "CLASS b = " , b.__class__
#print "CLASS a = " , a.__class__
#print dir(Person)
#print dir(Manager)
print dir(Manager.giveRaise)
print dir(Person.giveRaise)
print Manager.giveRaise.__repr__()
print Person.giveRaise.__repr__()
print Manager.giveRaise.__sizeof__()
print Person.giveRaise.__sizeof__()
#print help(Person.giveRaise.__sizeof__)
#print help(Person.giveRaise.__cmp__)
#print help(Person.giveRaise.__reduce__)
#print help(Person.giveRaise.__cmp__)
print Manager.giveRaise.__cmp__(Person.giveRaise)
print Manager.giveRaise.__cmp__(Manager.giveRaise)

print Person.giveRaise.__cmp__(Manager.giveRaise)


def ololo(k = 9):
    print "oloo"
    return "sad"


if (Person.__dict__) == (Manager.__dict__):
    print "OK"
else:
    print "NOK"

print issubclass(Manager, Person)
print locals()
#Anolog vars & __dict__
print vars(Person)
print Person.__dict__

#FOR CLASS COMPARE
keyyy = sorted((Person.__dict__))
key2 = sorted((Manager.__dict__))
print "KEYS  " , keyyy
#print globals()
k = [1, 4, 'b', [4, 7], ]
for i in keyyy:
    for j in key2:
        if i == j : print "OK   " , i

#FOR METHODS COMPARE
#keyyy = sorted(dict(Person.giveRaise))
#key2 = sorted(vars(Manager.giveRaise))
#key2 = sorted(dict(Person.lastName))

#print "KEYS  " , keyyy
#print globals()
#k = [1, 4, 'b', [4, 7], ]
#for i in keyyy:
#    for j in key2:
#        if i == j : print "OK   " , i

print len(keyyy)
print len(key2)
print filter(ololo, k)# return arg from k, if def ololo is True

print inspect.getmembers(a)