from aithris-object import *
def test1():
    return nlchk(None)
def test2():
    return nlchk("df")
print(str(test1()) + '\n end of test1' +'\n' + str(test2())+ '\n end of test2')
blocky = Element()
doc = HTMLBlock()
eTypes = ['b','div','b','nav','p','div']
eClass = ['colBox','Stretchy','colBox','longPanel','colPanel','closeBox']
for z in range(0,6):
    blocky.Id = 'Sparkling' + str(z) 
    blocky.Type = "b"
    # id , we don't need a stinkin id, thats the idea behind nullable objects.
    blocky.Class= eClass[z]
    blocky.Content='Chorus:<br/>\n'
    for i in range(1,5):   
        blocky.Content += '<h'+str(i)+'>'+ 'This is line ' + str(i) + ' indeed, '+str(i)+' feel fine' + '</h' + str(i) +'>'+'<br/>\n'
    doc.add(blocky)    
    blocky = Element()
saveText("testo.html",doc.get())
