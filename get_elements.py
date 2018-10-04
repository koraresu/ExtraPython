def inpu(first, second):
	inp = lambda a,b: [i for i in a if not i in b]
	first  = list( first )
	second = list( second )
	return ''.join( inp( first, second)+inp( second, first) )
def show_diferent_character(a,b):
	common = []
	z = list(a)+list(b)
	print( check )
	for x in range( len( a ) ):
		for y in range( len( b ) ):
			if a[x] == b[y]:
				common.append( a[x] )
				common.append( b[y] )
				break
	
	c = [ i for i in z if not i in common ]
	return ''.join( c )
def search(a,b):
	common = []
	add_common = lambda i: common.append( i )
	def add_common( i ):
		common.append( i )
	[ add_common( v ) for i,v in enumerate( list(a) ) if not v in b   ]
	for i,v in enumerate( list( a ) ):
		if not v in b:
			add_common( v )

	[ add_common( v ) for i,v in enumerate( list(b) ) if not v in a   ]
	return common
print( search("abc", "bcd") )
print( show_diferent_character("abc","bcd") )
print( inpu("abc", "bcd") )


