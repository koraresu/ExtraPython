class Node():
	parent = 0
	left   = 0
	right  = 0
	def set_left(self, node):
		self.left = node
	def set_right(self, node):
		self.right = node
a = [10, 12, 15, 18, 1, 5, 2,9,3,7]


tmp = 0
n = 0
for i in range(0, len(a)):
	if tmp == 0:
		n = Node()
		n.parent = a[i]
		tmp = 1
	elif tmp == 1:
		n.set_left = a[i]
		tmp = 2
	elif tmp == 2:
		n.set_right = a[i]
		tmp = 0
	
	n.parent = a[i]

