import heapq
import numpy as np
def get_numpy(file):
	v = np.loadtxt(open(file), delimiter=',')
	v = list( set( v ) )
	return heapq.nlargest(3, v)
print( get_numpy( 'stream.txt' ) )