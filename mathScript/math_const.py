__author__ = 'katrin'
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import *
import sys, os
def math_const(*args, **kwargs):

    try:
        #str = raw_input()
        #str1 = raw_input()
        #str = sys.argv[1]
        #str = args[0]
        str = str.split(':')
        const = eval(str[0])
        t = int(str[1])
        print (('%.' + str[1].strip()+ 'f') % const) #function return decimal view
        return ('%.' + str[1].strip()+ 'f') % const
    except NameError:
        print "Error"
    except ValueError:
        print "Error"
    except IndexError:
        print "Error"



if __name__ == '__main__':

    math_const('pi:4')
    math_const('e:19')
    math_const('er:19')
