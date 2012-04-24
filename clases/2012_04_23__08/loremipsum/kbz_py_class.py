class Basket(object):
	def __init__(self, contents=None):
		self.contents = contents or []
			
	def add(self, element):
		self.contents.append(element)
			
	def print_me(self):
		print 'Contains ' + ' '.join(self.contents)
		
# luego ejecutar esto
'''
my_instance=Basket(['1','2','3'])
my_instance.print_me()
'''