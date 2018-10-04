import random
s = 1000000
with open('stream.txt','a') as f:
	for i in range(0, s):
		f.write(',' + str( random.randint(1, 100000) ) )