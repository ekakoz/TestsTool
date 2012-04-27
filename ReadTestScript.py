__author__ = 'katrin'
import os
class ReadNameScripts:

    def __init__(self, dirName = '.'):
        self.__dirName =  dirName or []

    def pathProject(self):
        result = []
        import sys
        result = os.path.split(sys.path[0])
        result = result[0] + '/' #+ result[1]
        return result

    def listScripts(self):
        result = []
        for root, dirs, files in os.walk(self.__dirName):
            for name in files:
                fullname = os.path.join(root, name)
                result.append(fullname)
        return result

    def listScriptsNames(self):
        result = []
        for root, dirs, files in os.walk(self.__dirName):
            for name in files:
                
                (n , s)= os.path.splitext(str(name))
                if s == '.py':
                    result.append(n)

        return result

    def __str__(self):
        self.pathScript = []

        self.result=(self.listScripts())
        for each in self.result:
            self.pathScript.append(each)
            print  each
        return str()        #?


import string
def my_import(name):
    mod = __import__(name)
    components = string.split(name, '.')
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod


if __name__ == "__main__":
    k = ReadNameScripts('/home/katrin/PycharmProjects/TestTool/tests/')
   # print k.listScriptsNames()

    import inspect
    print inspect.getsource(ReadNameScripts)
    l= inspect.getargspec(my_import)
    print type(l)
    print l
    print inspect.getmoduleinfo('ReadNameScript.py')
    print __name__

