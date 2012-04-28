#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'katrin'

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
        return "Ololo"
    except ValueError:
        print "Error"
        return "Ololo"
    except IndexError:
        print "Error"
        return "Error"


