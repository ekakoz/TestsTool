import test_math_dir

__author__ = 'katrin'

import unittest, importlib, subprocess, sys, ReadTestScript

class TestToolHelp(unittest.TestCase):

#    def __init__(self, name):
#        self.module = importlib.import_module(name)
    def __init__(self, name, path):
        self.module = importlib.import_module(name, path)
        self.path = path
        self.name = name
        self.dir = str(sys.path[0])

    def runScript(self):
        scr = ReadTestScript.ReadNameScripts('dir')
        dirpath = scr.pathProject()
        self.process = subprocess.Popen(['python', dirpath + self.path + '/' + self.name+'.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        return self.process

    def runScriptArg(self, arg):
        scr = ReadTestScript.ReadNameScripts('dir')
        dirpath = scr.pathProject()
        self.process = subprocess.Popen(['python', dirpath + self.path +'/'+ self.name+'.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        self.process.stdin.write(arg)
        self.process.stdin.close()
        self.line = self.process.stdout.read()
        return self.line

    def assertFunction(self, arg):

        #imp = importlib.import_module('math_const', 'mathScript')

        return unittest.TestCase('run').assertEqual(str(type(eval('self.module.'+arg))), "<type 'function'>")

   #def assertType(self, arg):
    #    return unittest.TestCase('run').assertEqual(str(type(arg)), "<type 'function'>")

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

if __name__ == "__main__":
    k = TestToolHelp('math_const', 'mathScript')




