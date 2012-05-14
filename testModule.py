__author__ = 'Kozlova Ekaterina'
import test_math_dir

import unittest, importlib, subprocess, sys, ReadTestScript, inspect

class TestToolHelp(unittest.TestCase):

    def __init__(self, name, path = '.' ):
        """
        Constructor - main mission import module. It use name and path from arguments
        """
        self.path = path
        self.name = name
        self.dir = str(sys.path[0])
        self.module = importlib.import_module(name, path)

    def add_desc_task(self, *args, **kwargs):
        """
        This method run script from parameters and add result of this script to "*_task,txt" file
        *.txt file - it is file with description of task for student;
        this name must be similar to sampler script from teacher and must have ".txt" extension.

        """
        try:
            ans = []
            mark = []
            file_description = open(self.name + '_task.txt', "a") #open file for appending log - file with task

            for i in  range(len(eval('self.module.' + self.name + '.test'))):
                mark.append(eval('self.module.' + self.name + '.test' + str([i])))
                f = ret_function((mark[i]['grade']))
                f2 = f(eval('self.module.' + self.name))
                f3 = f2((mark[i]['in']))
                ans.append(f3)
                log = "\n>>> " + str(self.name) + "(" + mark[i]['in'] + ")"  +"\n" \
                + str(f3[0])
                file_description.write(log)
            file_description.close()
            return True
        except:
            return "Error add_desc_task"

    def runScriptArg(self, arg):
        scr = ReadTestScript.ReadNameScripts('dir')
        dirpath = scr.pathProject()
        self.process = subprocess.Popen(['python', dirpath + self.path +'/'+ self.name+'.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        self.process.stdin.write(arg)
        self.process.stdin.close()
        self.line = self.process.stdout.read()
        return self.line

    def run_def(self, curRun):
        """

        """
        file = open('log.txt', 'a')
        l = str(eval('self.module.' + curRun))
        print l
        file.write('>>' + curRun + '\n')
        file.write(l + '\n')

        file.close()

    def assertType(self, arg, typeRes):
        """
        This method asserts that "arg" from testing module is similar to typeRes.

        """
        return unittest.TestCase('run').assertEqual(str(type(eval('self.module.'+arg))), ("<type '"+ typeRes + "'>"))

    def report(self, function_name, student):
        """
        This method run, compare and generate report of scripts.

        """
        ans = []
        grade = 0
        mark = []
        total_grade = 0
        file_grade = open((str(student.name)+'.log'),"w")
        for i in  range(len(eval('self.module.' + function_name + '.test'))):
            print i
            mark.append(eval('self.module.' + function_name + '.test' + str([i])))
            f = ret_function((mark[i]['grade']))
            f2 = f(eval('self.module.' + function_name))
            f3 = f2((mark[i]['in']))
            total_grade = total_grade + mark[i]['grade']
            ans.append(f3)
        cur_grade = 0
        print "ans[] = " , (ans)
        for i in range(0, len(ans), 1):
            f = dec_call(ans[i][1], ans[i][0])
            f2 =f(eval('student.module.' + function_name))
            f3 = f2((mark[i]['in']))
            file_grade.write(str(i+1) + '.\t')
            mark[i]['grade'] = (mark[i]['grade'] * 100 )/total_grade
            file_grade.write((function_name + " RUN WITH ARGS: (" + \
                              str(mark[i]['in']) + "); POINT = " + str((mark[i]['grade']))) + '\n')  #run line

            if f3 == 0:
                file_grade.write("Expected result: " + ans[i][0] + '\n')
            else:
                f3 = f3 * 100 / total_grade
                file_grade.write("YOUR POINT = " + str(f3) + "\n")


            grade = grade + f3

        file_grade.write("\nRESULT GRADE = " + str(grade))
        file_grade.close()

    @staticmethod
    def report_run_TC():
        """
        This static method for run Test Cases from teacher and logging it to log file.
        This is 1 iteration.

        """
        imp = importlib.import_module('test_math_dir', 'tests')
        list = sys.argv[2:] # list of arguments from command line
        if list <> []:
            dir = list[2]
        else:
            dir = str(sys.path[0])
        scr = ReadTestScript.ReadNameScripts(dir)
        s = sys.path
        log_file = str(sys.path[0]) + '/report_run_TC.txt'
        f = open(log_file, "a") #open file for appending log
        p = scr.listScriptsNames()
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
    print "TYPE:\t\t", type(item)
    #print "VALUE:\t\t", repr(item)
    if str(type(item)) == "<type 'function'>":
        print "ARGSPEC:\t", inspect.getargspec(item)
    print "CALLABLE:\t",

    if callable(item):
        print "Yes"
    else:
        print "No"

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
            dict_member[key] = inspect.getargspec(eval('item.' + key))

        elif str(type(eval('item.' + key))) == "<type 'classobj'>":
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
                    print "type" , type(task[i][key].defaults[0])#temprory. I want to know about type of arguments
                    log = open(key , "w")
                    log.write("SAMPLER " + str(sampler[i][key]) + "\n")
                    log.write("STUDENT " + str(task[i][key]) + "\n")
                    log.close()
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


def cmp_copy_file(file1, copy_file1):
    try:
        import filecmp
        res = filecmp.cmp(file, copy_file1)
        return res
    except Exception as e:
        return e

def run_auto_check(*args):
    """
    This function begin the process of automatic tests.

    """
    try:

        if len(args) == 2:
            sampler = TestToolHelp(args[0])
            sampler_data =  interspect(sampler.module)
            student = TestToolHelp(args[1])
            student_data = interspect(student.module)
            if (cmp_function(sampler_data, student_data)):
                sampler.report(sampler.name, student)
            else:
                return "Error: False compare sampler and student scripts"
        elif len(args) == 1:
            sampler = TestToolHelp(args[0])
            sampler_data =  interspect(sampler.module)
            file_sampler_info = open(sampler.name + '.info', "w")
            file_sampler_info.write("{FUNCTION INFO} {CLASS INFO} {METHODS INFO}\n\n")
            file_sampler_info.write(str(sampler_data))
            file_sampler_info.close()
            sampler.add_desc_task()
        else:
            return "Error: count of arguments - 1 or 2."

    except :
        return "Unexpected error!"

if __name__ == "__main__":
    run_auto_check('math_const')
    run_auto_check('math_const', 'math_const_2')

