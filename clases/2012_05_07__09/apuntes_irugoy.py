class Basket (object):
    def __init__(self, contents=None):
        self.contents = contents or []
        
    def add (self,element):
        self.contents.append(element)
        
    def print_me(self):
        print 'Contains ' + ' '.join(self.contents) 
    
    def __str__(self):
        print 'Contains ' + ' '.join(self.contents)
        
    def __del__(self):
        print 'Delete ' + ' '.join(self.contents) 
     
     
   
#Una tupla es inmutable, una vez creada no puede ser cambiado su valor en tiempo de ejecucion
('Gut','Carl')

#Una lista puede ser alterada en tiempo de ejecucion
['Gut','Carl']

#Un diccionario tiene claves y valores
{'esta es la clave':'Carl', 'esta es otra clave': 'otro valor'}

#Como concatenar un texto con muchas variables adicionales
'El nombre de esta persona es %s.' % 'Appelido'

'El nombre de esta persona es %s, %s' % ('Appelido', 'Nombre')

'El nombre de esta persona es %(n)s, %(a)s' % {'a':'Gut','n':'Carl'}

#Booleanos se escriben con capitular
True
False

#Short-circuit con condicionales and y or
True and True #En el and si el primer valor valida a true entonces devuelve el segundo valor de lo contrario devuelve el primero
True or True #En el or si el primer valor valida a true entonces devuelve dicho valor sino el segundo

#Para armar un paquete de modulos de Python solo hay que crear un archivo __init__.py "vacio" dentro de la carpeta donde residen los modulos

#Modulos mas comunes en Python
    # pip - Python Installer Package
    # virtualenv - Modulo de ambiente virtual para desarrollo de Python
    # bpython - Consola Python mejorada
    # fabric - Sirve para automatizar scripts que corren en entornos localales y remotos
    # pil - Libreria de imagenes
    # beautifulsoup - Mamejador de HTML dom basico

#Modulo de Python es un archivo ejecutable de Python con codigo dentro
