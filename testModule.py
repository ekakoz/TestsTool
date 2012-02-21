import test_math_dir

__author__ = 'katrin'

import unittest, importlib, subprocess, sys, ReadTestScript

class TestToolHelp(unittest.TestCase):

    def __init__(self, name):
        self.module = importlib.import_module(name)
        self.name = name

    def runScript(self):
        self.process = subprocess.Popen(['python', '/home/katrin/PycharmProjects/TestTool/math/'+ self.name+'.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        return self.process

    def runScriptArg(self, arg):
        self.process = subprocess.Popen(['python', '/home/katrin/PycharmProjects/TestTool/math/'+ self.name+'.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        self.process.stdin.write(arg)
        self.process.stdin.close()
        self.line = self.process.stdout.read()
        return self.line

    def assertFunction(self, arg):
        return unittest.TestCase('run').assertEqual(str(type(self)), "<type 'function'>")

    #def assertType(self, arg):
    #    return unittest.TestCase('run').assertEqual(str(type(arg)), "<type 'function'>")

    @staticmethod
    def report():
        list = sys.argv[2:] # list of arguments from command line
        if list <> []:
            dir = list[2]
        else:
            dir = '/home/katrin/PycharmProjects/TestTool/tests/'
        scr = ReadTestScript.ReadNameScripts(dir)
        log_file = '/home/katrin/PycharmProjects/TestTool/report.txt'
        f = open(log_file, "a") #open file for appending log

    #runner = unittest.TextTestRunner(f, verbosity=2)

        for each in scr.listScriptsNames():
            #f.writelines("\n" + str(each) + "\n")
            l = unittest.TestLoader().loadTestsFromTestCase(test_math_dir.TestCase)
            
            for line in unittest.TestLoader().loadTestsFromTestCase(test_math_dir.TestCase):
                res = unittest.TestResult()
                unittest.TextTestRunner(verbosity=2).run(line)

        del sys.argv[0:]

if __name__ == "__main__":
    k = TestToolHelp('math_const')



