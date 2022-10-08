import math
from . import Num, Sym
import re

class Cols:

    # Initialize new Sym class object
    def __init__(self, names, all=[], klass=0,x=[],y=[]):
        self.names = names
        self.all = all
        self.klass = klass
        self.x = x
        self.y = y

        for key in names:

            columnName=names[key]
            columnObj={}
            startsWithUppercase=re.match("^[A-Z]*",columnName)
            if startsWithUppercase:
                num=Num.Num(key, columnName)
                columnObj=num
                self.all.append(columnObj)
            else:
                sym=Sym.Sym(key, columnName)
                columnObj=sym
                self.all.append(columnObj)

            columnSkipped=re.match(":$",columnName)
            if not columnSkipped:
                goalColumn=re.match("[!+-]]",columnName)
                if goalColumn:
                    self.y.append(columnObj)
                else:
                    self.x.append(columnObj)

            singleDependentKlassColumn=re.match("!$",columnName)
            if singleDependentKlassColumn:
                self.klass=columnObj


