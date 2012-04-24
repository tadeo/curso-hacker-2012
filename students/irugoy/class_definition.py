class Basket (object):
    def __init__(self, contents=None):
        self.contents = contents or []
        
    def add (self,element):
        self.contents.append(element)
        
    def print_me(self):
        print 'Contains ' + ' '.join(self.contents) 