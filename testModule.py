import test_math_dir

__author__ = 'katrin'

import unittest, importlib, subprocess, sys, ReadTestScript, inspect

class TestToolHelp(unittest.TestCase):

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

    def report_2(self, function_name, student):
        ans = []
        grade = 0
        mark = []
        file_grade = open((str(student.name)+'.log'),"w")
        for i in  range(len(eval('self.module.' + function_name + '.test'))):
            print i
            mark.append(eval('self.module.' + function_name + '.test' + str([i])))
            print "PPPP" , mark
            f = ret_function((mark[i]['grade']))
            f2 = f(eval('self.module.' + function_name))
            f3 = f2((mark[i]['in']))
            ans.append(f3)
        print type(mark)
        print "ans[] = " , (ans)
        for i in range(0, len(ans), 1):

            f = dec_call(ans[i][1], ans[i][0])
            f2 =f(eval('student.module.' + function_name))
            f3 = f2((mark[i]['in']))
            file_grade.write(str(i+1) + '.\t')
            #print "MARK" , mark[:1]
            file_grade.write((function_name + " RUN WITH ARGS: (" + (mark[i]['in']) + "); POINT = " + str((mark[i]['grade']))) + '\n')  #run line
            file_grade.write("POINT = " + str(f3) + "\n")
            if f3 == 0:
                #print ("Expected result: " + ans[i][0] + '\n')
                file_grade.write("Expected result: " + ans[i][0] + '\n')
            grade = grade + f3
        file_grade.write("\nRESULT GRADE = " + str(grade))
        file_grade.close()
#    def report_2(self, task, student):
#        file = open(task, "r")
#        mark = []
#        ans = []
#        grade = 0
#
#        file_grade = open((str(student.name)+'.log'),"w")
#
#        for line in file:
#            #print line
#            line = (line.split('~'))
#            mark.append(line)
#
#        #Run sampler script and remember answers to ans []
#
#        for i in range(0, len(mark), 1):
#            #print "name" , mark[i][0] ,"run with args", mark[i][1]  #run line
#            f = ret_function(int(mark[i][2]))
#            f2 = f(eval('self.module.' + mark[i][0]))
#            f3 = f2(eval(mark[i][1]))
#            print "f3 = " , f3[0]
#            ans.append(f3)
#            print "ans[] = " , ans[0][0]
#            #print "Answer = " , ans[i]
#
#        #Then run student script and compare with sampler answers
#        for i in range(0, len(mark), 1):
#            file_grade.write(str(i+1) + '.\t')
#            file_grade.write(mark[i][0] + " run with args " + mark[i][1] + " point = " + str(int(mark[i][2])) + '\n')  #run line
#            f = dec_call(ans[i][1], ans[i][0])
#
#
#            f2 =f(eval('student.module.' + mark[i][0]))
#            #Run student script with args
#            f3 = f2(eval(mark[i][1]))
#            file_grade.write("POINT = " + str(f3) + "\n")
#            if f3 == 0:
#                file_grade.write("Expected result: " + ans[i][0] + '\n')
#            grade = grade + f3
#
#
#        file_grade.write("\nRESULT GRADE = " + str(grade))
#
#        file_grade.close()
#        file.close()


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
def dec_call(fn, point, ans):
    """Decorator compare answers.
    It is return summary point for one run (with one set of arguments)
    It works with function.

    """
    def wrap(*args, **kwargs):
        try:
            if fn(*args, **kwargs) == ans:
                print "NAME:\t" , fn.__name__ , args , ' = ' , point
                return point
            t = inspect.getargspec(fn)
            print dir(t)
            print t
            print "Zero POINT"
            grade = 0
            return grade
        except :
            print "NAME (- point):\t" , fn.__name__ , args , ' = ' , point
            print inspect.getargspec(fn)
            grade = 0
            return grade
    return wrap

@decorator_for_decorator
def ret_function(fn, point):
    def wrap (*args, **kwargs):

        return fn(*args, **kwargs), point
    return wrap

#
#def return_members(item):
#    member = []
#    dict =  item.module.__dict__
#
#    for key in dict:
#        t = type(eval('tempScript.module.' + key))
#        if str(t) == "<type 'function'>":
#            print "User function = " , key
#            print (eval('tempScript.module.' + key))

def interrogate(item):
    """return useful information about item.

    """
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

def interrogate2(item):
    """return useful information about module.

    """
    information = []
    if hasattr(item, '__name__'):
        print "NAME:\t\t", item.__name__
        information.append(item.__name__)
    if hasattr(item, '__class__'):
        print "CLASS:\t\t", item.__class__.__name__
        information.append(item.__class__.__name__)

#        print information[0]
#    print type(item)
#    dict =  item.__dict__
#    print "STR = " , str(item.name)
#    print "STR - module = " , (str(eval(item.module + '.math_const')))
#    for key in dict:
#        t = type(eval('item.module.' + key))
#        if str(t) == "<type 'function'>":
#            print "User function = " , key
#            fn = (eval('item.module.' + key))
#            print "ArgSpec: " , inspect.getargspec(fn)
#        elif str(t) == "<type 'class'>":
#            print "Class: " , key

    #print "Module Info:  " , inspect.getmoduleinfo(information[0])
    #print "ID:\t\t\t", id(item)
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

def interspect(item):
    """Return module info.
    This function return information about module.
    It contains functions name with arguments or Classes names with methods.

    """
    if hasattr(item, '__name__'):
        print "NAME: " , item.__name__
    dict_member = {}
    class_member = {}
    method_member = {}
    for key in dir(item):
        if str(type(eval('item.' + key))) == "<type 'function'>":
            #print "KEY: ", key
            #print "ARGS: ", inspect.getargspec(eval('item.' + key))
            dict_member[key] = inspect.getargspec(eval('item.' + key))

        elif str(type(eval('item.' + key))) == "<type 'classobj'>":
            #print "KEY: ", key
            class_member[key] =  eval('dir(item.' + key + ')')
            for k in class_member[key]:
                if str(type(eval('item.' + key + '.' + k))) == "<type 'instancemethod'>":
                    method_member [k]=  (inspect.getargspec((eval('item.' + key + '.' + k))))

    return dict_member, class_member, method_member

def cmp_function(sampler, task):
    result = False
    for i in range(3):
        for key in sampler[i]:
            if key in task[i]:
                if len(sampler[i][key].args) == len(task[i][key].args):
                    result = True
                elif len(sampler[i][key].args) <= len(task[i][key].args):
                    print "STUDENT " , task[i][key]
                    print "sampler " , sampler[i][key]
                    return False
                elif (task[i][key].varargs) <> None :
                    result = True
                elif (task[i][key].keywords) <> None:
                    result = True
                else :

                    return  False

            else:
                print "nok"
                return False

    return True



if __name__ == "__main__":
    sampler = TestToolHelp('math_const')
    sampler_data =  interspect(sampler.module)
    stud = TestToolHelp('math_const_2')
    stud_data = interspect(stud.module)
    print sampler.module.math_const.test
    sampler_class = TestToolHelp('simple_class')

    if (cmp_function(sampler_data, stud_data)):
        sampler.report_2(sampler.name, stud)
        #sampler.report_2('run_math.txt', stud )
    else:
        print "FALSE COMPARE"

    #print interspect(sampler_class.module)


#    stud = 'math_const_2'
#    teacher = 'class_for_testing'
#    m = importlib.import_module(stud)
#    interspect(m)
#    cl = importlib.import_module(teacher)
    #run_math.txt - file with function names and arguments. Now it is parted via "<"
#Comment only now..
#    sampler.report_2('run_math.txt',  sampler.module, stud )
    #module = importlib.import_module(name, path)
#    tempScript = TestToolHelp('math_const')
#    interrogate(interrogate2)
    #interrogate2(tempScript.module)
#    tempScrClass = TestToolHelp('class_for_testing')
#    interrogate2(tempScrClass)

        #<function interrogate at 0x2a388c0>
        #print eval('tempScript.module.' + key)

    #print inspect.getmoduleinfo(tempScript.path)
#    interrogate(t.module)

    ################################################




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

