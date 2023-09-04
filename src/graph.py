"""
graph.py
Utah Tech Undergrduate Research

Represent nodes with integers. If you want non-integers, translate it yourelf lol


"""
from dataclasses import dataclass
def debug(*a,**kw):
  print(*a,**kw)

class Node:
  """Class for keeping track of visitation state and value"""
  def __init__(self,weight,visited=False):
    self.weight = weight
    self.visited = visited
  def __str__(self):
    return f"{self.weight}{'T' if self.visited else 'F'}"


class Graph:
  """Class for adding, removing, and traversing nodes in a graph"""

  def __init__(self, node_count:int, * , directed:bool=False, weighted:bool=False):
    self.matrix: list = [[Node(0) for _ in range(node_count)] for _ in range(node_count)]
    self.weighted = weighted
    #^ create a 2-D grid of nodes and their possible connections.


  def connect(self,a: int, b: int, * , weight=1):
    self.matrix[a][b].weight = weight;
    return self

  # this doesn't work. I do not know why yet.
  def depth_first(self,start,callback):
    for source, node in self._from_enumerate(start):
      for connection, node_obj in enumerate(node):
        if node_obj.visited or node_obj.weight == 0:
          self.matrix[source][connection].visited = True
          continue
        self.matrix[source][connection].visited = True
        if self.weighted:
          callback(source,connection,node_obj.weight)
        else:
          callback(source,connection)
        if connection != start and source != start:
          print(f"exploring {connection}")
          self.depth_first(connection,callback)
    return self


  def breadth_first(self,start,callback):
    ...


  def __len__(self):
    return len(self.matrix)


  def __str__(self):
    res= ""
    for node in self.matrix:
      res += ' '.join(str(other) for other in node)
      res += '\n'
    return res


  def _from(self,node):
    return map(self.matrix.__getitem__,range(node,len(self)))


  def _from_enumerate(self,node):
    get_value = self.matrix.__getitem__
    length    = len(self)
    return zip(range(length),map(get_value,range(node,length)))


def test():
  my_graph = Graph(5)
  my_graph.connect(0,0).connect(0,1).connect(1,1).connect(2,2).connect(3,3).connect(4,4)
  print(my_graph)
  def callback(source,connection):
    print(f"connection from {source} to {connection}")
  my_graph.depth_first(0,callback)

test()
