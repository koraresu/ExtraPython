"""
class Nodo:

	def __init__(self, name=None, prox=None):
		self.name = name
		self.prox = prox
	def __str__(self):
		return str( self.name )

def verLista(nodo):
	while nodo:
		print( nodo )
		nodo = nodo.prox


v3 = Nodo("Bananas")
v2 = Nodo("Peras", v3)
v1 = Nodo("Manzanas", v2)


verLista( v3 )
"""

a = [10,34,3,5,6,7,6,1,2]
#print( [n for i , n in enumerate(a) if n in a[i+1:] and n not in a[:i]][0] )

x = []
for i,n in enumerate(a):
	if (n in a[i+1]):
		x.append( n)

print( x )