'''

Python introduction
Based on Appendix A of the book "Beginning Python - From Novice To Professional" fromo Apress publishing

'''
import this # The Zen of Python, by Tim Peters

################
#  Assignment  #
################

x = 42
x, y, z = 1, 2, 3

first, second = 'a', 'b'
first, second = second, first

a = b = 'test string'

# Warning: b = 'test string' does not return a value!



#############################
#  Blocks with indentation  #
#############################

if x < 5 or (10 < x and x < 20):
    print 'ok'

if x < 5 or 10 < x < 20:
    print 'ok'

for i in [1, 2, 3, 4, 5]:
    print 'Number: ', i

x = 10
while x >= 0:
    print 'x is still not negative.'
    x = x-1 # equivalent to x -= 1

for value in range(100):
    print value # prints from 0 to 99 inclusive



#####################
# String formatting #
#####################

x = input('Enter a number: ')
print 'The square of the number is', x*x
print 'The square of the number is' + str(x*x)
print 'The square of the number is %s' % x*x
print 'The square of %s is %s' % (x, x*x)
print 'The square of %(number)s is %(result)s' % {'number': x, 'result': x*x}



#########
# Lists #
#########

name = ['Doe', 'John']
print name[1], name[0]
name[0] = 'Smith'
x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
x[5:7] # [5, 6] > x[i:j] j is exclusive
x[5:] # [5, 6, 7, 8]
x[:5] # [0, 1, 2, 3, 4]

y = x # makes a reference
y[1] = 0
print x # [0, 0, 2, 3, 4, 5, 6, 7, 8]
y[1] = 1

z = x[:] # makes a copy
z[1] = 0
print x # [0, 1, 2, 3, 4, 5, 6, 7, 8]

x[-1] # 8

len(x) # 9

x.append(9)
print x
del x[9]

x[7:9]=[0, 0] # [0, 1, 2, 3, 4, 5, 6, 0, 0]
x.count(0) # 3
x.index(0) # 0
x.index(0, 1) # 7
x.index(0, 1, 3) # ValueError: list.index(x): x not in list
del x[7:9]
x.extend([7, 8]) # equivalent to x += [7, 8]

x.pop(1) # 1
x.pop(10) # IndexError: pop index out of range
x.pop() # 8
x.insert(1, 1)
x.insert(8, 8)
x.reverse() # in place does not return a value



################
# Dictionaries #
################

person = {'name': 'John', 'last_name': 'Doe'}
person['name'] = 'Peter'
person['name'] # 'Peter'
person['name'] = 'John'
person['middle'] # KeyError: 'middle'
person.get('middle') # None safer way to ask for a dictionary key
person.get('middle', 'Charles') # 'Charles'
person.update({'middle': 'Charles'}) # in place does not return a value

person.pop('name', )

person.items() # [('last_name', 'Doe'), ('name', 'Peter')]
for k, v in person.items():
    print k, v

person.keys() # ['last_name', 'name']
person.values() # ['Doe', 'Peter']

for k in person: # equivalent to 'for k in person.keys():'
    print k

person_copy = person.copy()

person.has_key('name')
person.has_key('street')

person.clear()

###############
# Duck typing #
###############

"If it walks like a duck, and talks like a duck, it’s a duck."


#################
# sha hash note #
#################
import hashlib
hashlib.sha1('Content to be hashed to a 40 chars length hexa string').hexdigest()

