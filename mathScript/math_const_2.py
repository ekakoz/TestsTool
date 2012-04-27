#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'katrin'
"""Temporary file
Create for training working with module inspect.
"""
from math import *
import sys, os
def math_const(str="pi:5"):

    try:
        str = str.split(':')
        const = eval(str[0])
        t = int(str[1])
        print (('%.' + str[1].strip()+ 'f') % const) #function return decimal view
        return ('%.' + str[1].strip()+ 'f') % const
    except NameError:
        print "Error"
        return False
    except ValueError:
        print "Error"
    except IndexError:
        print "Error"


def introspection(item):
    """Print useful information about item."""
    if hasattr(item, '__name__'):
        print "NAME:\t\t", item.__name__
    if hasattr(item, '__class__'):
        print "CLASS:\t\t", item.__class__.__name__
    print "ID:\t\t\t", id(item)
    print "TYPE:\t\t", type(item)
    print "VALUE:\t\t", repr(item)
    if str(type(item)) == "<type 'function'>":
        print "ARGSPEC:\t", inspect.getargspec(item)
    print "CALLABLE:\t",

    if callable(item):
        print "Yes"
    else:
        print "No"

    f = inspect.currentframe()
    print inspect.getargvalues(f)


if __name__ == '__main__':
    #math_const()
    #cmd = 'python ' + str(sys.argv[1]) + str(sys.argv[2])


    math_const("pi:4")
    math_const("pil:5")
    print "+++++++++++++++++++"
    print math_const.__class__.__dict__
    print "+++++++++++++++++++"

    import inspect
    print inspect.getargspec(math_const)
    introspection(math_const)
    print "____________\n"
    introspection(3)
    u = inspect.currentframe()
    print u
    print "____________\n"
    print "sys._getframe()" , sys._getframe()
    print "math_const.func_defaults" , math_const.func_defaults