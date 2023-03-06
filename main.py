from tubemap import tubemap
from pathfind import Pathfinding
from random import randint

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
    station1 = pf.data.get_vertex(station_input_data[int(input("Station 1: "))])
    station2 = pf.data.get_vertex(station_input_data[int(input("Station 2: "))])
    break
  except:
    pass

for vertex in pf.data.vertices:
  pf.compute_vertex_neighbours(vertex, tubemap[vertex.data])

paths = pf.find(station1, station2)

paths.sort(key=len)

print(f"Paths({len(paths)}):\n\n")

for path in paths[:5]:
  print(" -> ".join([station.data for station in path]))
  print("\n\n")

funpaths = []

for station1 in station_input_data.values():
  for station2 in station_input_data.values():
    if station1 == station2: continue
    paths = pf.find(pf.data.get_vertex(station1), pf.data.get_vertex(station2))
    funpaths.append((station1, station2, len(paths)))
    if randint(0,10) == 4: print(len(funpaths))

funpaths.sort(key=[2])
print(funpaths[:10])