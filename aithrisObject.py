from aithris-functional import *
from aithris-generic import *

def nlchk(value):
    if (value != "" and value != None):
        return 1
    else:
        return -1

class HTML:
    Doctype = ""
class Element:
    Type = ""
    Id = ""
    Class = ""
    Content = ""
    Index = -1
    def get(self):
        txt = ""
        if (self.Type != ""):
            txt += '<' + self.Type
            if (nlchk(self.Id)==1):
                txt += ' id="' + self.Id + '" '
            if (nlchk(self.Class)==1):
                txt += ' class="' + self.Class +'"'
            if (nlchk(self.Content)==1):
                txt += '>\n' + self.Content + '\n</' + self.Type + '>'
            else:
                txt += '>' + '' + '</' + self.Type + '>'
            return txt
        else:
            return ""
#End Element
class HTMLBlock:
    Elements = []
    def add(self,element):
        if (element.get!=""):
            if (len(self.Elements) >= 0 ):
                element.Index = len(self.Elements)+1
                self.Elements.append(element)
            else:
                this.Elements[0]=element
            return ""

                

    def get(self):
        txt = ""
        for x in self.Elements:
            txt+='/n'
            txt+=x.get()
        return txt
#End HTMLBlock
       
    
class CSSBlock:
    Selector = ""
    Rules = []
    Comments = []
    def add(self,rule):
        if (nlchk(rule)==1):
            self.Rules.append()
            return ""
    def add(self,comment):
        if (nlchk(comment)==1):
            self.Comments.append()
            return ""
        
                
#End CSSBlock  
class DebugLog:
    Log = list()
    Times = list()
    def add(item):
        if (nlchk(item)==1):
            Times.append(str(mktime()))
            Log.append(item)
            return ""
        else:
            Times.append(str(mktime()))
            Log.append("Invalid Blank Entry")
            return "0"
#End DebugLog
#class HTMLForm(HTMLBlock):



#End HTMLForm

class File():
    Filename = ""
    Elements = list()
    




        

##################################################################################################################
##
##                                                                                                              ##
##                                                                                                              ##
##bIG FRIGGIN TO DO LIST                                                                                                              ##
##                                                                                                              ##
##  1. FORM OBJECT                                                                                              ##
##  2. complete json object and functional                                                                      ##                                           ##   
##  3. Convert nlchk to use bool, true fals, 0,1, anything but -1 and 1                                         ##  
##  4. Write conplete tests and or testing platform for the various library stuff, especially the generics.     ##
###