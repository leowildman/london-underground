from tubemap import tubemap
from pathfind import Pathfinding
from random import randint
from threading import Thread

#1. Write code that will ask the user to enter two valid London Underground stations and...
#2. Calculate all possible routes between those two stations without visiting the same station more than once on that route
#3. Output the total number of possible routes
#4. Output the top 5 routes (in terms of fewest number of station stops)

#Extension: Modify the underlying graph representation to include details about which 'line/s' each connected station is connected by. Then update your algorithm to additionally output the top 5 routes in terms of fewest line changes (and if it is a tie, then by total number of stops)

def get(station1, funpaths, pf):
    for station2 in station_input_data.values():
        if station1 == station2: continue
        paths = pf.find(pf.data.get_vertex(station1), pf.data.get_vertex(station2))
        funpaths.append((station1, station2, len(paths)))
        
        print(f"{station1}: {station2}")

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
threads = []

for station1 in station_input_data.values():
 t = Thread(target=get, args=(station1, funpaths, pf))
 t.start()
 threads.append(t)
 print(f"Thread {station1} started.")
 
for t in threads:
    t.join()
    
 


for path in funpaths:
    if path[2] >80000: print(path)