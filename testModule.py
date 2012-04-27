import test_math_dir

__author__ = 'katrin'

import unittest, importlib, subprocess, sys, ReadTestScript, inspect

class TestToolHelp(unittest.TestCase):

#    def __init__(self, name):
#        self.module = importlib.import_module(name)
#        name = name of file with script
#        path = default is current directory, else current_directory/next

    def __init__(self, name, path = '.' ):
        self.path = path
        self.name = name
        self.dir = str(sys.path[0])
        self.module = importlib.import_module(name, path)

    def run_script(self, *args, **kwargs):
        #scr = ReadTestScript.ReadNameScripts('dir')
        #dirpath = scr.pathProject()
        #execfile('math_const.py')
        f = open('math_const_task.txt', "a") #open file for appending log - file with task
        l = subprocess.check_output(['python', self.dir + '/'  + self.name+'.py'])
        #l = subprocess.Popen(['python', self.dir + '/' + self.path + '/' + self.name+'.py'], stdout=subprocess.PIPE)
        print '====='
        print l
        print '====='
        #f.write('\n' + str(self.name) + ':\n')
        f.write(l)
        f.close()

#    def run_script(self):
#        scr = ReadTestScript.ReadNameScripts('dir')
#        dirpath = scr.pathProject()
#        self.process = subprocess.Popen(['python', dirpath + self.path + '/' + self.name+'.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
#        return self.process

    def runScriptArg(self, arg):
        scr = ReadTestScript.ReadNameScripts('dir')
        dirpath = scr.pathProject()
        self.process = subprocess.Popen(['python', dirpath + self.path +'/'+ self.name+'.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        self.process.stdin.write(arg)
        self.process.stdin.close()
        self.line = self.process.stdout.read()
        return self.line

    def run_def(self, curRun):
        file = open('log.txt', 'a')
        l = str(eval('self.module.' + curRun))
        print l
        file.write('>>' + curRun + '\n')
        file.write(l + '\n')

        file.close()

    def assertFunction(self, arg):

        #imp = importlib.import_module('math_const', 'mathScript')

        return unittest.TestCase('run').assertEqual(str(type(eval('self.module.'+arg))), "<type 'function'>")


    def assertType(self, arg, typeRes):
        return unittest.TestCase('run').assertEqual(str(type(eval('self.module.'+arg))), ("<type '"+ typeRes + "'>"))


    #@staticmethod
    def report_2(self, task, script):
        f = open(task, "r")
        mark = []
        for line in f:
            #print line
            line = (line.split('<'))
            mark.append(line)
        print len(mark)
        for i in range(0, len(mark), 1):

            print "name" , mark[i][0] ,"run with args", mark[i][1]  #run line
            l = dec_call(2)
            print "L = " , l
            l2 = l(eval('self.module.' + mark[i][0]))
            print "L2 = " , l2
            l3 = l2(eval(mark[i][1]))
            print "L3 = " , l3

            #ret_function - return result of function
            l = ret_function(2)
            #print "R = " , l
            l2 = l(eval('self.module.' + mark[i][0]))
            #print "R2 = " , l2
            l3 = l2(eval(mark[i][1]))
            print "R3 = " , l3


        f.close()
            #printf mark[i][1] #mark line

    @staticmethod
    def report():
        imp = importlib.import_module('test_math_dir', 'tests')
        list = sys.argv[2:] # list of arguments from command line
        if list <> []:
            dir = list[2]
        else:
            dir = str(sys.path[0])
        scr = ReadTestScript.ReadNameScripts(dir)
        s = sys.path
        log_file = str(sys.path[0]) + '/report.txt'
        f = open(log_file, "a") #open file for appending log
        p = scr.listScriptsNames()
        #runner = unittest.TextTestRunner(f, verbosity=2)
        #p1 = scr.listScriptsNames()
        for each in scr.listScriptsNames():
            f.writelines("\n\n" + str(each) + "\n")
            l = unittest.TestLoader().loadTestsFromTestCase(imp.TestCase)
            res = 0
            n = 0
            for line in unittest.TestLoader().loadTestsFromTestCase(imp.TestCase):
                k = unittest.TextTestRunner(verbosity=2).run(line)
                n = n + 1
                if k.wasSuccessful():
                    res = res + 1
                    f.writelines(str(line._testMethodName))
                    f.writelines(" -\t1\n\n")
                else:
                    f.writelines(str(line._testMethodName))
                    f.writelines(" -\t0\n\n")
            f.write("Result = " + str(res) + "/" + str(n) + "\n")
            f.writelines("___________")
        del sys.argv[0:]
def decorator_for_decorator(decor):
    """Create decorator
    This function is used as decorator.
    It decorates another function, which must be a decorator.
    This function get one argument. It will be used to estimate students work.

    """
    def decorator_creater(*args, **kwargs):
        def decorator_wrap(fn):
            return decor(fn, *args, **kwargs)
        return decorator_wrap
    return decorator_creater


@decorator_for_decorator
def dec_call(fn, point):
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

@decorator_for_decorator
def ret_function(fn, point):
    def wrap (*args, **kwargs):
        return fn(*args, **kwargs)
    return wrap

@ret_function(1)
def ololol2():
    return "ERROR"

print ololol2()
@dec_call(1)
def ololo(a = 5, b = 6):
    print "OLOOLOOOLOOO"



def interrogate(item):
    """Print useful information about item."""
    if hasattr(item, '__name__'):
        print "NAME:\t\t", item.__name__
    if hasattr(item, '__class__'):
        print "CLASS:\t\t", item.__class__.__name__
    print "ID:\t\t\t", id(item)
    print "TYPE:\t\t", type(item)
    #print "VALUE:\t\t", repr(item)
    if str(type(item)) == "<type 'function'>":
        print "ARGSPEC:\t", inspect.getargspec(item)
    print "CALLABLE:\t",

    if callable(item):
        print "Yes"
    else:
        print "No"

import ReadTestScript

def temporary(a = 5):
    print "OK"

if __name__ == "__main__":
    t = TestToolHelp('math_const')
#    t.report_2('run_math.txt', t.name)
#    t.run_def('math_const(\'er:19\')')
#    t.module.math_const('er:19')
    t.report_2('run_math.txt', t.module)
    interrogate(t.module)

    ################################################

    #print ololo(5, 6 ,'0')
    #print ololo()

    l = dec_call(2)
    l2 = l(temporary)
    l3 = l2()


#    script_files = ReadTestScript.ReadNameScripts('tests')
#    print type(ReadTestScript)
#    print inspect.getmembers(script_files)
#
#    list_script = script_files.listScripts()
#    print type(list_script)
#
#    for each in list_script:
#        l = TestToolHelp('test_math_dir', 'tests')
#        print l.name
#    print '++++++++++++++++'
#    k = TestToolHelp('math_const', 'mathScript')
#    k.run_script()
#    interrogate(k.module)
#    l = inspect.getmodule(k.module)
#
#    source_script = inspect.getsource(eval('k.module.' + k.name))
#    print "source_script = inspect.getsource______________________"
#    print source_script
#    print 'inspect.getmodule' + str(l)
#    print 'get module   ' + str(inspect.getmodule(k))
#    print 'get module info    ' + str(inspect.getmoduleinfo(k.path))
#    #print 'get call args   ' + str(inspect.getcallargs(k.module.math_const))
#    print 'get args spec   ' + str(inspect.getargspec(eval('k.module.' + k.name)))
#    print '********************************************************'
#    print dir(k.module)
#    t = False
#    print type(inspect.getsourcelines(k.module))
#    for line in inspect.getsourcelines(k.module):
#        if str(type(line)) == '<type \'list\'>':
#
#            for each in line:
#                if str(each) == "if __name__ == '__main__':\n":
#                    t = True
#                    print "TRUE"
#                if t == True:
#
#                    print each

