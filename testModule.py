__author__ = 'Kozlova Ekaterina'

import test_math_dir

import unittest, importlib, subprocess, sys, ReadTestScript, inspect

class TestToolHelp(unittest.TestCase):

    def __init__(self, name, path = '.' ):
        """
        Constructor - main mission of this method imports module. It use name and path from arguments

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
        If that file is not exist yet, this method will create it.

        """
        try:
            ans = []
            mark = []
            f_name = args[0]
            file_description = open(self.name + '_task.txt', "a") #open file for appending log - file with task

            for i in  range(len(eval('self.module.' + f_name + '.test'))):
                mark.append(eval('self.module.' + f_name + '.test' + str([i])))
                f = ret_function((mark[i]['grade'])) #grade, int
                if str(type(eval('self.module.' + f_name))) == "<type 'classobj'>": # this for work with classes
                    f2 = f(eval('self.module.' + f_name))
                    ret = self.__get_args__(mark[i]['in'][f_name])
                    f3 = eval("f2(" + ret + ")")
                    log = "\n>>> " + str(f_name) + "(" + ret + ")"  +"\n" \
                                                            + str(f3[0])
                    file_description.write(log)
                    for meth in range(len(mark[i]['in']) - 1): #now call methods
                        m = mark[i]['in'].keys()[meth+1]
                        ret = self.__get_args__(mark[i]['in'][m])
                        f_cl2 = f(eval('f3[0].' + m)) #methods
                        f_cl3 = eval("f_cl2(" + ret + ")") #arg of methods
                        ans.append(f_cl3)
                        log = "\n>>> " + str( mark[i]['in'].keys()[meth+1]) + "(" + ret + ")"  +"\n" \
                                        + str(f_cl3[0])
                        file_description.write(log)

                else: # work with usual functions
                    f2 = f(eval('self.module.' + f_name))#function
                f3 = None
                #if str(type(mark[i]['in'])) == "<type 'str'>":
                if type(mark[i]['in']) == str:
                    f3 = f2(mark[i]['in']) #mark[i]['in'] it is argument.
                    ans.append(f3)
                elif len((mark[i]['in'])) == 1:
                    f3 = f2(mark[i]['in'])
                    ans.append(f3)
                else:
                    ret = self.__get_args__(mark[i]['in'])
                    f3 = eval("f2(" + ret + ")")
                    ans.append(f3)
                if f_cl3 <> None:
                    print "ok"
                else:
                    log = "\n>>> " + str(f_name) + "(" + str(mark[i]['in']) + ")"  +"\n" \
                + str(f3[0])
                    print ans
                    file_description.write(log)
            file_description.close()
            return True
        except Exception as e:
            return "Error add_desc_task"

    def __get_args__(self, list_args = []):
        res = ""
        for key in list_args:
            if type(key) == str:
                res = res + "\"" + str(key) + "\", "
            else:
                res = res + str(key) + ", "
        res = res[:-2]
        #print "RES " + res
        return res

    def __run_def__(self, curRun):
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
        file_grade = open((str(student.module.__name__)+'.log'),"w")
        for i in  range(len(eval('self.module.' + function_name + '.test'))):
            mark.append(eval('self.module.' + function_name + '.test' + str([i])))
            f = ret_function((mark[i]['grade']))
            f2 = f(eval('self.module.' + function_name))
            f3 = f2((mark[i]['in']))
            total_grade = total_grade + mark[i]['grade']
            ans.append(f3)
        print "ans[] = " , (ans)

        for i in range(0, len(ans), 1):
            f = dec_call(ans[i][1], ans[i][0])
            f2 =f(eval('student.module.' + function_name))
            f3 = f2((mark[i]['in']))
            file_grade.write(str(i+1) + '.\t')
            file_grade.write((function_name + " RUN WITH ARGS: (" + \
                              str(mark[i]['in']) + "); POINT = " + str((mark[i]['grade']))) + '\n')  #run line

            if f3 == 0:
                file_grade.write("Expected result: " + str(ans[i][0]) + '\n')
            else:
                file_grade.write("YOUR POINT = " + str(f3) + "\n")

            grade = (grade + f3)
        file_grade.write("\nRESULT GRADE = " + str(grade))
        file_grade.close()

    def run_class(self, *args):
        mark = []
        ans = []
        sampler_data = args[0]
        file_descriptor = open("OLOLO.txt", "w")
        print len(sampler_data[1])
        class_name = sampler_data[1].keys()
        inst_cl = eval('self.module.' + class_name[0])
        print type(inst_cl)
        print eval('self.module.' + class_name[0] + '.test')
        len_1 = len(eval('self.module.' + class_name[0] + '.test'))
        for i in  range(len_1):

            mark.append(eval('self.module.' + class_name[0] + '.test' + str([i])))
            print 'self.module.' + class_name[0] + '.test' + str([i])
            cl = ret_function((mark[i]['grade']))
            len_in = len(eval('self.module.' + class_name[0] + '.test[' +str(i) + "]" + "['in']"))
            for key in range():
                print key
#            cl2 = cl(eval('self.module.' + self.name))
#            cl3 = cl2((mark[i]['in']))
#            ans.append(f3)
#            log = "\n>>> " + str(self.name) + "(" + mark[i]['in'] + ")"  +"\n" \
#            + str(f3[0])
#            file_description.write(log)
#            file_description.close()
#            return True


#            for s in range(len(Person.test)):#import module!!!
#                print "_______"
#                for key in Person.test[s]['in']:
#                    a = key + "("
#                    b = False
#                    for i in Person.test[s]['in'][key]:
#                        t = str(i) + str(type(i))
#                        if type(i) == str:
#                            a = a + "\"" + i + "\", "
#                        else:
#                            a = a + str(i) + ", "
#                        b = True
#                    if b == True:
#                        a = a[0:-2] + ")"
#                        b = False
#                    else:
#                        a = a + ")"
#                    print a

    @staticmethod
    def report_run_TC():
        """
        This static method for run Test Cases from teacher and logging it to log file.
        Syntax of Test Cases like syntax in unit.
        This is first iteration.

        """
        imp = importlib.import_module('test_math_dir', 'tests')
        list = sys.argv[2:] # list of arguments from command line
        if list <> []:
            dir = list[2]
        else:
            dir = str(sys.path[0])
        scr = ReadTestScript.ReadNameScripts(dir)
        #s = sys.path
        log_file = str(sys.path[0]) + '/report_run_TC.txt'
        f = open(log_file, "a") #open file for appending log
        #p = scr.listScriptsNames()
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
                return point
            t = inspect.getargspec(fn)
            grade = 0
            return grade
        except :
            grade = 0
            return grade
    return wrap
#
#@decorator_for_decorator
#def ret_class(cl, point):
#    def wrap(*args, **kwargs):
#        return cl(*args, **kwargs), point
#    return wrap


@decorator_for_decorator
def ret_function(fn, point):
    def wrap (*args, **kwargs):
        return fn(*args, **kwargs), point
    return wrap

def interspect(item):
    """Return module info.
    This function return information about module.
    It contains functions name with arguments or Classes names with methods.

    """
    if hasattr(item, '__name__'):
        print "NAME: " , item.__name__
    print type(item)
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
                    return True
                elif len(sampler[i][key].args) <= len(task[i][key].args):
                    #type" , type(task[i][key].defaults[0])#temprory. I want to know about type of arguments
                    log = open(key + '_compare' , "w")
                    log.write("Compare of two function is FALSE.\n")
                    log.write("SAMPLER " + str(sampler[i][key]) + "\n")
                    log.write("STUDENT " + str(task[i][key]) + "\n")
                    log.close()
                    return False
                elif (task[i][key].varargs) <> None :
                    result =  True
                elif (task[i][key].keywords) <> None:
                    result = True
                else :
                    return  False
            else:
                print "nok cmp_function" #debug message
                return False
    return result


def cmp_copy_file(file1, copy_file1):
    try:
        import filecmp
        res = filecmp.cmp(file, copy_file1)
        return res
    except Exception as e:
        return e

def compare_Class(sampler, task):
    """
    Compare two class: sampler from teacher and task from student.
    Student task must contain >= count of methods with the same name to sampler.

    """
    for key in sampler[1]:
        print key
    #return True

def run_auto_check(*args):
    """
    This function begin the process of automatic tests.

    """
    try:

        if len(args) == 2:
            sampler = TestToolHelp(args[0])
            sampler_data =  interspect(sampler.module)
            sampler.name = sampler_data[0].keys()[0]
            student = TestToolHelp(args[1])
            student_data = interspect(student.module)
            student.name = student_data[0].keys()[0]

            # first "if" for run compare two functions and after that run check teacher and student functions.
            if sampler_data[0] <> None:
                if (cmp_function(sampler_data, student_data)):
                    sampler.report(sampler.name, student)
                else:
                    stud_log = open(student.module.__name__ + ".log", "w")
                    stud_log.write("Definitions in your script is wrong.\nYour GRADE = 0.")
                    stud_log.close()
                    return "Error: False compare sampler and student scripts"
        elif len(args) == 1:
            sampler = TestToolHelp(args[0])
            sampler_data =  interspect(sampler.module)
            file_sampler_info = open(sampler.name + '.info', "w")
            file_sampler_info.write("{FUNCTION INFO} {CLASS INFO} {METHODS INFO}\n\n")
            file_sampler_info.write(str(sampler_data))
            file_sampler_info.close()

            if sampler_data[0]<>{}:
                sampler.add_desc_task(sampler_data[0].keys()[0]) #add description to file with task
            elif sampler_data[1] <> {}:
                sampler.add_desc_task(sampler_data[1].keys()[0])
        else:
            return "Error: count of arguments - 1 or 2."

    except Exception as e:
        return "Unexpected error!" + e

if __name__ == "__main__":

    """Now we have work variant for function with one argument
    TC; math_const - sampler
    math_const_2-6 - SUT

    """
    #run_auto_check('math_const')
    #run_auto_check('sampler_sum')
    #run_auto_check('math_const', 'math_const_4')
    #run_auto_check('sampler_strToSock', 'strToSock_03')
    #run_auto_check('sampler_strToSock')
    run_auto_check('person_class')
#    sampler = TestToolHelp('math_const')
#    sampler_data =  interspect(sampler.module)
#    student = TestToolHelp('math_const_2')
#    student_data = interspect(student.module)
#    res = cmp_function(sampler_data, student_data)
#    print res