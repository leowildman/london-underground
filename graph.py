class Graph:
    def __init__(self):
        self.vertices = []

    def add_vertex(self, data):
      vertex_to_add = Vertex(data)
      self.vertices.append(vertex_to_add)
      return vertex_to_add

    def add_edge(self, vertex1, vertex2, weight=1):
      edge = Edge(vertex1, vertex2, weight)
      vertex1.connected_edges.append(edge)
      if vertex1 not in vertex2.neighbours:
        vertex2.neighbours.append(vertex1)
      if vertex2 not in vertex1.neighbours:
        vertex1.neighbours.append(vertex2)
      return edge

    def remove_vertex(self, vertex):
      for neighbour in vertex.neighbours:
        neighbour.neighbours.remove(vertex)
        for edge in neighbour.connected_edges:
          if edge.vertex == vertex:
            neighbour.connected_edges.remove(edge)
            break
      self.vertices.remove(vertex)

    def remove_edge(self, vertex, edge):
      vertex.connected_edges.remove(edge)
      
    def get_vertex(self, data):
      for vertex in self.vertices:
        if vertex.data == data:
          return vertex
      return None
      
    def __repr__(self):
      pass


class Vertex:
    def __init__(self, data):
        self.data = data
        self.connected_edges = []
        self.neighbours = []
    def __repr__(self):
      return f"data: {self.data} edges: {self.connected_edges}"

class Edge:
  def __init__(self, Vertex1, Vertex2, weight):
    self.vertex1 = Vertex1
    self.vertex2 = Vertex2
    self.weight = weight

  def __repr__(self):
    return (f"{self.vertex1.data}:{self.vertex2.data}")
