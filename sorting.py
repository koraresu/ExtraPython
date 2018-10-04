def quicksort(vector):
	if not vector:
		return []
	else:
		pivote = vector[-1]

		menor = [ x for x in vector if x < pivote ]
		mayor = [ x for x in vector[:-1] if x >= pivote ]
		
		return quicksort(menor) + [pivote] + quicksort(mayor)
def gnome_sort(vector):
	i_b = 1
	i_i = 2
	taille = len( vector )
	while i_b < taille:
		if vector[i_b-1] <= vector[i_b]:
			i_b, i_i = i_i, i_i+1
		else:
			vector[i_b-1], vector[i_b] = vector[i_b] , vector[i_b-1]
			i_b -=1
			if i_b == 0:
				i_b, i_i = i_i, i_i+1
	return vector
def bubble_sort(vector):
	permutation = True
	iteration   = 0
	while permutation == True:
		permutation = False
		iteration = iteration+1
		for actual in range(0, len( vector) + iteration):
			print( vector )
			try:
				if vector[actual] > vector[actual+1]:
					permutation = True
					vector[actual], vector[actual+1] = vector[actual+1], vector[actual]
			except:
				pass
	return vector
def merge_sort(vector):
	print( vector[0:len(vector)//2] )
	print( vector[len(vector)//2:len(vector)] )

element = [ 12, 3, 19, 18, 1, 17, 6, 8, 20, 7, 16, 5, 15, 13, 10, 2, 11, 9, 14, 4 ]
#print( quicksort( element ))
#print( gnome_sort( element ) )
#print( bubble_sort( element ) )
print( merge_sort( element ) )
#print( insertion_sort( element ) )