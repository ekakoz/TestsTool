__author__ = 'katrin'
import os
class ReadNameScripts:

    def __init__(self, dirName = None):
        self.__dirName =  dirName or []

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
    import importlib
  