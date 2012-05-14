#!/usr/bin/env python

class Basket (object):
    ''' Esta es una clase Basket '''

    print __doc__

    def __init__(self, contents=None):
        self.contents = contents or []

    def add (self,element):
        self.contents.append(element)

    def mark_as_locked(self):
        self.locked = True

    def __str__(self):
        if self.contents:
            return '[%s]' % (', '.join(map(str, self.contents)),)
        else:
            return 'No objects'

    def __unicode__(self):
        return u'Contains ' + u' '.join(map(unicode, self.contents))

#if __name__ == '__main__':
#    basket1 = Basket([1,2,3])
#    print '1er print: %s' % basket1
#    basket2 = Basket()
#    print '2do print: %s' % basket2
#    basket3 = Basket([basket1, basket2])
#    print '3do print: %s' % basket3
