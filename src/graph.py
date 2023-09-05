"""
graph.py
Utah Tech Undergrduate Research

Represent nodes with integers. If you want non-integers, translate it yourelf lol


"""
RED = lambda s: f"\x1B[1;31m{s}\x1B[0m"
GRN = lambda s: f"\x1B[1;32m{s}\x1B[0m"
from dataclasses import dataclass
def debug(*a,**kw):
  print(*a,**kw)

class Node:
  """Class for keeping track of visitation state and value"""
  def __init__(self,weight,visited=False):
    self.weight = weight
    self.visited = visited
  def __str__(self):
    return f"{self.weight}{GRN('T') if self.visited else RED('F')}"


class Graph:
  """Class for adding, removing, and traversing nodes in a graph"""

  def __init__(self, node_count:int, * , directed:bool=False, weighted:bool=False):
    self.matrix: list = [[Node(0) for _ in range(node_count)] for _ in range(node_count)]
    self.weighted = weighted
    #^ create a 2-D grid of nodes and their possible connections.


  def reset(self,*,visited=True,weight=True):
    for nodelist in self.matrix:
      for node in nodelist:
        node.visited = not visited
        node.weight  = int(not weight)
    return self


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

  def depth_first_2(self,start,callback):
    for src, node_list in self._from_enumerate(start): # this will loop through each ROW starting at START, zipped with an index.
      for dst, node_obj in enumerate(node_list):       # this will loop through each COLUMN, skipping anything that has already been visited OR is not a connection.
        if node_obj.weight == 0:
          continue
        if node_obj.visited:
          continue
        else:
          node_obj.visited = True
          callback(src,dst)
          self.depth_first_2(dst,callback)
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
    return res[:-1]


  def _from(self,node):
    return map(self.matrix.__getitem__,range(node,len(self)))


  def _from_enumerate(self,node):
    get_value = self.matrix.__getitem__
    length    = len(self)
    return zip(range(length),map(get_value,range(node,length)))


def print_expected_path(list_of_connections):
  print('->'.join(f"({c[0]},{c[1]})" for c in list_of_connections))

def build_graph(my_graph,connections):
  my_graph.reset()
  [my_graph.connect(*e) for e in connections]
  return my_graph

def test_sequential(my_graph):
  connections = [(0,0),(0,1),(1,0),(0,2),(0,3),(0,4)]
  print_expected_path(connections)
  build_graph(my_graph,connections)
  callback = lambda s,d: print(my_graph,end="\n\n")
  my_graph.depth_first_2(0,callback)

def test_back_and_forth(my_graph):
  connections = [(0,2),(2,0),(0,3),(3,0),(0,4),(4,1)]
  print_expected_path(connections)
  build_graph(my_graph,connections)
  callback = lambda s,d: print(my_graph,end="\n\n")
  my_graph.depth_first_2(0,callback)

def test_no_connections(my_graph):
  connections = [(0,0),(0,1),(0,2),(0,3),(4,0),(4,1)]
  print_expected_path(connections)
  build_graph(my_graph,connections)
  callback = lambda s,d: print(my_graph,end="\n\n")
  my_graph.depth_first_2(0,callback)

def test():
  my_graph = Graph(5)
  test_sequential(my_graph)
  test_back_and_forth(my_graph)
  test_no_connections(my_graph)

test()
