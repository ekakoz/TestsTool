# -*- coding: utf-8 -*-
__author__ = 'katrin'
import inspect, sys

def decorator_for_decorator(decor):
    """Create decorator
    This function is used as decorator.
    It decorates another function, which must be a decorator.
    This function get one argument. It will be used to estimate students work.

    """
    def decorator_creator(*args, **kwargs):
        """return decorator_creator.
        *args and **kwars - received arguments
        """
        def decorator_wrap(fn):
            """wrapper
            Decorator must be always this type of:
            decor(fn, *args, **kwargs)
            """
            return decor(fn, *args, **kwargs)
        return decorator_wrap
    return decorator_creator


@decorator_for_decorator
def dec(fn, point):
    """
    a  - for point
    """
    def wrap(*args, **kwargs):
        try:
            if fn(*args, **kwargs) == True:
                print "NAME:\t" , fn.__name__ , args , ' = ' , point
            return point
        except :
            print "NAME:\t" , fn.__name__ , args , ' = ' , point
            print inspect.getargspec(fn)
            return -point
    return wrap

@dec(1)
def temp_func(a = 5, b = 6):
    print "temp func"

print temp_func(5, 6 ,'0')
print temp_func()

def temporary(a = 5):
    print "OK"

t = dec(10)
t2 = t(temporary)
t3 = t2(6, 7, 8)

print "temporary function with decorator - dec" , t3

t = dec(2)
t2 = t(temporary)
t3 = t2()

print t3

t = dec(3)
t2 = t(temporary)
t3 = t2(8)

print t3
