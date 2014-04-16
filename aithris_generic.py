class Debugable():
    def __init__(self):
        self.Debug = false
    Debug = false
    def DebugOn():
        Debug = true
    def DebugOff():
        Debug = false
## begin loggable
class Loggable(Debugable):
    def __init__(self):
        self.data.clear
    data = list()
    def log(self, text):
        data.append(text)
## end loggable
## begin valuable
class Valueable(Loggable):
    def __init__(self):
        self.data.clear
    Value = null
    def get(self):
        return self.Value
    def set(self, value):
        self.Value = value
#end value
##begin nameable
class Nameable(Valueable):
    def __init__(self):
        self.data.clear
    Name = null
    
##end nameable
# begin variable
class Variable(Nameable):
        def __init__(self):
            self.Value = null    
            self.Type = null
        Type = null


#end variable
## begin Compareable
class Compareable(Variable):
    def __init__(self):
        self.Compared = false
    def Compare(self, term):
        self.Compared = true
        if(self.Value==term):
            return true
            else
            return false
        Compared = false
    def EndComparison(self):
        self.Compared = false
##End Compareable


class Element(Compareable):
        def __init__(self, begin, end):
            self.Open = begin
            self.Close = end
        Open  = ""
        Close = ""
        

#begin container
class Container(Variable):
    def __init__(self,begin,delim,end):
        self.Begin = begin
        self.End = end
        self.Delim = delim
        self.Variables.clear()
    Variables = list()
    def set(self, Variables):
        try:
            if(Variables.count<=0):
                self.Variables.append(Variables)
            else:
                self.Variables.clear()
                self.Variables.append(Variables)
        except e:
            self.log(e)
       
    def add(item):
        self.Variables.append(item)
    def read():
        text = self.Begin
        last = len(self.Variables) - 1
        for i, item in Variables:
            if(i<last):
                text+=item+self.Delim+'\n'
            else:
                text+=item + '\n' + self.End
        return text
    def remove(item):
        try:
            self.Variables.remove(item)
            return ''
        except e:
            return e
#end container    
    



