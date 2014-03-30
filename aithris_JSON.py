
class Object():
    Elements = list()
    Begin = '{'
    End = '}'
    Delim = ","
    Quote = ""
    def add(self,item):
        Elements.append(item)
    def get(self):
        body = ""
        Foreach(item in Elements)
        body += self.Begin + self.Quote + self.Item + self.Quote + self.End + self.Quote
class Array():
    Elements = list()
    Begin = '['
    End = ']'
    Delim = ','
