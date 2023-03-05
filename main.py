from tubemap import tubemap
from pathfind import Pathfinding

#1. Write code that will ask the user to enter two valid London Underground stations and...
#2. Calculate all possible routes between those two stations without visiting the same station more than once on that route
#3. Output the total number of possible routes
#4. Output the top 5 routes (in terms of fewest number of station stops)

#Extension: Modify the underlying graph representation to include details about which 'line/s' each connected station is connected by. Then update your algorithm to additionally output the top 5 routes in terms of fewest line changes (and if it is a tie, then by total number of stops)

stations = tubemap.keys()
station_input_data = dict((i, j) for i, j in enumerate(stations))
print(station_input_data)

pf = Pathfinding()

print("Select two stations from this list.")
for index, station in station_input_data.items():
  pf.add(station)
  print(f"{index}: {station}")

while 1:
  try:
    station1 = station_input_data[int(input("Station 1: "))]
    station2 = station_input_data[int(input("Station 2: "))]
    break
  except:
    pass

print(tubemap["Aldgate"])
print(pf.data.vertices)
for vertex in pf.data.vertices:
  pf.compute_vertex_neighbours(vertex, tubemap[vertex.data])

print(pf.data.get_vertex("Liverpool Street"))