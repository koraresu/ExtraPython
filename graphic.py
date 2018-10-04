from collections import defaultdict
class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def setNode(self, value):
    self.nodes.add(value)

  def set_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance


def dijsktra(graph, initial, final):
    nodes = graph.nodes
    edges = graph.edges
    
dij = Graph()
dij.setNode('0')
dij.setNode('1')
dij.setNode('7')
dij.setNode('2')
dij.setNode('8')
dij.setNode('6')
dij.setNode('3')
dij.setNode('5')
dij.setNode('4')

dij.set_edge( '0' , '1' , 4 )
dij.set_edge( '0' , '7' , 8 )
dij.set_edge( '1' , '7' , 11 )
dij.set_edge( '7' , '8' , 7 )
dij.set_edge( '8' , '6' , 6 )
dij.set_edge( '7' , '6' , 1 )
dij.set_edge( '2' , '8' , 2 )
dij.set_edge( '2' , '5' , 4 )
dij.set_edge( '3' , '5' , 14 )
dij.set_edge( '3' , '4' , 9 )
dij.set_edge( '5' , '4' , 10 )


print( dijsktra( dij , '0','8') )