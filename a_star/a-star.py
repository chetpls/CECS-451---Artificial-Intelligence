import math
import sys

#parse through coordinates.txt and save city, lat, long to a set
def readCoords():
    cities = {}
    with open("coordinates.txt", "r") as f:
        for line in f:
            cityName, coords= line.strip().split(":")
            lat, long = coords.strip("()").split(',')
            cities[cityName] = {"lat":float(lat), "long":float(long)}
    return cities

#haversine formula to calculate the the straight line distance
def haversine(lat1, long1, lat2, long2):
    latDiff = (toRadian(lat2) - toRadian(lat1))/ 2
    longDiff = (toRadian(long2) - toRadian(long1)) / 2
    root = math.sin(latDiff)**2 + math.cos(toRadian(lat1)) * math.cos(toRadian(lat2)) * math.sin(longDiff)**2
    sqroot = math.sqrt(root)
    distance = 2 * 3958.8 * math.asin(sqroot)
    return distance

#converts degree to radian                   
def toRadian(n):
    return (n *(math.pi /180))

#parse through map.txt and save city with their neighbors and the cost to a set
def readMap():
    nodes = {}
    with open("map.txt", "r") as f:
        for line in f:
            cityName, neighbors = line.strip().split("-")
            cities = neighbors.split(",")
            nodes[cityName] = {"neighbors" : {}}
            for city in cities:
                name, cost = city.split("(")
                cost = float(cost.strip(")"))
                nodes[cityName]["neighbors"][name] = {"cost":cost} 
    return nodes

#returns the path
def path(cameFrom, current):
    path= current
    while current in cameFrom:
        current =cameFrom[current]
        path = str(current) + ' - ' + path
    return path

#a star algorithm that returns a string containing the start, end, path, and total miles
def a_star(start, end):
    distance = readCoords()
    nodes = readMap()
    #nodes that are already evaluated
    closedSet = set()
    #nodes to be evaluated
    openSet = {start}
    #path taken to reach the node
    cameFrom = {}
    #gScore = cost of path from start to node
    gScore = {node: float("inf") for node in nodes}
    gScore[start] = 0
    #fScore = gScore[n] + haversine(n), total estimated cost
    fScore= {node: float("inf") for node in nodes}
    fScore[start] = haversine(distance[start]['lat'], distance[start]["long"], distance[end]["lat"], distance[end]["long"])
    while len(openSet) > 0:
        #set the current node to the node with the lowest fScore value
        current_node = min(openSet, key = lambda node:fScore[node])
        #if current is the end, return start, end, best route and total distance
        if current_node == end:
            result = "From city: "+ start +"\nTo city: "+ end +"\nBest Route: "+ path(cameFrom,current_node)+"\nTotal distance: "+ "{:.2f}".format(round(fScore[end],2)) + " mi"
            return  result
        #manage which nodes have been evaluated
        openSet.remove(current_node)
        closedSet.add(current_node)
        #compute the cost for each neighbor of current node
        for neighbor, cost in nodes[current_node]["neighbors"].items():
            newcost = gScore[current_node] + cost["cost"]
            #save the new cost if its better than the previous one
            if  newcost < gScore[neighbor]:
                cameFrom[neighbor] = current_node
                gScore[neighbor] = newcost
                fScore[neighbor] = gScore[neighbor] + haversine(distance[neighbor]['lat'], distance[neighbor]["long"] , distance[end]["lat"], distance[end]["long"])
                if neighbor not in openSet:
                    openSet.add(neighbor)
    return None



print(a_star(str(sys.argv[1]), str(sys.argv[2])))













