#	2012 04 23
#	author: [kbz]: www.kbz.com.uy

my_lorem = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum'

def lorem_words (how_words):	
	words = my_lorem.split(' ')
	
	result = words[:how_words]
	return ' '.join(result)

lorem_words(5)