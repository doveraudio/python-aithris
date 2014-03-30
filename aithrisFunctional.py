from string import Template
from io import IOBase
from fileinput import *
from datetime import *
from time import *


    
def openPage(title,head):
    """Returns the opening tags for an html file. title: The title of the html being created. head: script and style declarations. See"""
    preSection = Template("""<!DOCTYPE html>
<html>
    <head>
        <title>$title</title>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        $head
        </head>
    <body>\n""")
    return preSection.substitute(title = title,head = head)

def closePage():
    """Returns the closing tags for an html file. It takes no parameters at this time."""
    return """    </body>
</html>"""

def addElement(HTMLelement, content):
    txt = Template('<$HTMLelement> $content </$HTMLelement>')
    return txt.substitute(cssClass = cssClass, HTMLelement = HTMLelement, content = content)
def addElement(cssClass, HTMLelement, content):
    txt = Template('<$HTMLelement class="$cssClass"> $content </$HTMLelement>')
    return txt.substitute(cssClass = cssClass, HTMLelement = HTMLelement, content = content)
    
def addElement(cssID, cssClass, HTMLelement, content):
    txt = Template('<$HTMLelement id="$cssID" class="$cssClass"> $content </$HTMLelement>')
    return txt.substitute(cssClass = cssClass, cssID = cssID, HTMLelement = HTMLelement, content = content)

    
def add():
    return None
def cssRule(selector, cssBlock):
    """Returns a formatted css rule. selector: requires a valid string naming """
    field = Template(
'''
$selector {
$cssBlock
}''')
    return field.substitute(selector = selector, cssblock = cssblock)
    
def css(property,value):
    """Returns a single css declaration, created by supplying a string to property, and value. See docs.. :roll:"""
    element = Template('$property:$value;')
    return element.substitute(property = property, value = value)

def fontFace(Family,Source,Additional):
    """Returns an @font-face css rule. 
    Parameters: 
        Family: Font name and basic properties, ie. 'Bitstream Vera Serif Bold'
        Source: The URL source of the font file
        Additional: Any additional rules that might be needed. Use css('property','value')"""
  
def addCssLink(filename):
    """Returns an html formatted link to an external css file. """
    csslink = Template('<link rel="stylesheet" type="text/css" href="$filename">')
    return csslink.substitute(filename = filename)
    
def addJsLink(filename):
    """Returns an html formatted link to an external javascript file"""
    jslink = Template('<link rel="script" type="text/javascript" src="$filename">')
    return jslink.substitute(filename = filename)
    
def saveText(filename,content):
    """Saves the input text to a file, in utf-8 format, with supplied filename"""
    
    if (filename==""):
        now = ctime(time())
        filename="default" + now
    with open(filename,"w", encoding="utf-8") as f:
        return f.write(content)
        
def openText(filename):
    with open(filename,"r", encoding="utf-8") as f:
        return f.read()
        
def formatText(filename):
    """Returns a block of text reformatted for reading, including basic indention. RUDIMENTARY DON'T JUDGE ME"""
    text = ""
    last = ""
    ltext = "</br>"
    tab = '&#160;'*4
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if (last == '</br>' or last == '\n' or ltext == '</br>' or ltext == '\n'):
                ltext = tab + line + '</br>'
            else:
                ltext = line + '</br>'
            text += ltext
            last = line
    return text




      
        
# end library
#example of how to use the library to construct a simple webpage, with a css page. no javascript yet.

#############################################################################################################
# from BoilerplateFactory import *
# fs = 'font-size'
# lfont = '22pt'
# mfont = '18pt'
# sfont = '12pt'
# HUGEFONT = '75pt'
# red = 'red'
# black ='black'
# white ='white'
# col = 'color'
# bcol = 'background-color'
# page = ""
# style  = "/*A script generated StyleSheet - made by dover */"
# page = openPage('The Quest of Iranon - A short story by H.P.Lovecraft</br>', addCssLink('style.css'))
# style = style + cssRule('Body', css(bcol,black) + '\n' + css(col,white) + '\n')
# page = page + addElement('navbar','nav','H.P.Lovecraft')
# page = page + addElement('titlebar bigfont','div', 'The Quest of Iranon </br>')
# page = page + addElement('author smallfont','b','short story by H.P.Lovecraft</br>')
# page = page + addElement('mainsection textfont','a', formatText('book.txt'))
# style = style + cssRule('.navbar', css(bcol,black) + '\n' + css(col,red) + '\n')
# style = style + cssRule('.bigfont', css(fs,lfont) + '\n')
# style = style + cssRule('.textfont', css(fs,mfont) + '\n')
# style = style + cssRule('.smallfont', css(fs,sfont) + '\n')
# style = style + cssRule('.titlebar', css(bcol,red) + '\n' + css(col,black) + '\n' + css('width','50%'))
# style = style + cssRule('.mainsection', css(bcol,black) + '\n' + css(col,white) + '\n')
# page = page + closePage()
# saveText('index.html',page)
# saveText('style.css',style)
# print(openText('index.html'))
# print(openText('style.css'))
###############################################################################################################



