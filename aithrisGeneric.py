class Loggable():
    def __init__(self):
        self.Data.clear
    Data = list()
    def log(text):
        Data.append(text)
class Element(Loggable):
    def __init__(self,begin,delim,end):
        self.Begin = begin
        self.Delim = delim
        self.End = end
    Begin=''
    Delim=''
    End=''
class Tuple(Loggable, Element):
    Name = ''
    Value = ''
    def set(self, name, value):
        self.Name = name
        self.Value = value
    def read(self):
        return self.Begin+self.Name+self.Delim+self.Value+self.End

class Container(Element):
    def __init__(self, begin,delim,end):
        self.Begin = begin
        self.End = end
        self.Delim = delim
        self.Elements.clear()
    Elements = list()
    Begin = ''
    End = ''
    Delim = ''
    def set(self, elements):
        try:
            if(elements.count<=0):
                self.Elements.clear()
            else:
                self.Elements.clear()
                self.Elements.append(elements)
        except e:
            self.log(e)
          
    def add(item):
        self.Elements.append(item)
    def read():
        text = self.Begin
        last = len(self.Elements) - 1
        for i, item in Elements:
            if(i<last):
                text+=item+self.Delim+'\n'
            else:
                text+=item + '\n' + self.End
        return text
    def remove(item):
        try:
            self.Elements.remove(item)
            return ''
        except e:
            return e
    
    



