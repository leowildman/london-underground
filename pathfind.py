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

  def find(self, start:Vertex, end):
    paths = []
    current_path = []
    current_vertex = start
    next_verticies = Stack(len(self.data.vertices))
    while 1:
      current_path = [start]
      for value in current_vertex.neighbours:
        if value in current_path: continue

        if value not in next_verticies:
          next_verticies.push(value)

        

      if current_vertex == end:
        paths.append(current_path)

      for 
        


  