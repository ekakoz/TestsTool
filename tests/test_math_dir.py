
import unittest
import sys
import StringIO, subprocess
#from test import in_raw
import  testModule
class TestCase(unittest.TestCase):

    def setUp(self):
        self.held, sys.stdout=sys.stdout, StringIO.StringIO()
        arg = []
        for line in arg[0:]:
            cmd = cmd + line


    def test_1(self):
#       module = testModule.TestToolHelp('math_const')
        module = testModule.TestToolHelp('math_const', 'mathScript')
        res = module.runScriptArg("pi:4")
        self.assertEquals(res,'3.14161\n')

    def test_2(self):
        module = testModule.TestToolHelp('math_const', 'mathScript')
        res = module.runScriptArg("pi:4")
        self.assertEquals(res,'3.1416\n')

    def test_3(self):
        script = testModule.TestToolHelp('math_const', 'mathScript')
        script.assertFunction('math_const')

    def test_4(self):
        script = testModule.TestToolHelp('math_const', 'mathScript')
        script.assertType('math_const', 'function')


if __name__ == '__main__':
    import importlib
    mod = importlib.import_module('testModule', 'TestTool')
    print mod
    mod.TestToolHelp.report( )
