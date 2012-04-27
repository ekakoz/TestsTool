#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'katrin'
version__ = "$Revision: 1$"
from math import *
import sys, os
"""Local copy from dir mathScript
"""
def math_const(str):#*args, **kwargs):

    try:
        #str = args[0]
        str = str.split(':')
        const = eval(str[0])
        t = int(str[1])
        print (('%.' + str[1].strip()+ 'f') % const) #function return decimal view
        return ('%.' + str[1].strip()+ 'f') % const
    except NameError:
        #print "Error"
        return "Error"
    except ValueError:
        #print "Error"
        return "Error"
    except IndexError:
        #print "Error"
        return "Error"





def interrogate(item):
    """Print useful information about item."""
    print __name__
    print '+++++++++++++'
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

#    f = inspect.currentframe()
 #   print inspect.getargvalues(f)

if __name__ == '__main__':

    #interrogate(3)
    #print __file__
    #print interrogate(3)
    #print dir(interrogate)
    #print 'math_const(\'pi:4\')'
    math_const('pi:4')
    math_const('e:19')
    math_const('er:19')
