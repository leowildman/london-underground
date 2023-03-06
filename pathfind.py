from graph import Graph, Vertex, Edge
from stack import Stack

class Pathfinding:
  def __init__(self):
    self.data = Graph()

  def add(self, item):
    self.data.add_vertex(item)

  def compute_vertex_neighbours(self, vertex, neighbours):
    for value in neighbours:
      self.data.add_edge(vertex, self.data.get_vertex(value))

  def find(self, start: Vertex, end: Vertex):
    paths = []
    stack = Stack(len(self.data.vertices))
    stack.push([start])
    while stack.peek() != None:
        path = stack.pop()
        node = path[-1]
        if node == end:
            paths.append(path)
        else:
            for adjacent in node.neighbours:
                if adjacent not in path:
                    new_path = list(path)
                    new_path.append(adjacent)
                    stack.push(new_path)
    return paths

        


  