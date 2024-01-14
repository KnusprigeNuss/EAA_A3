import random
import os
random.seed()

f = open("random_graph.txt", "w")

# random number of nodes between 100 and 300
number_of_vertices = random.randint(10, 300)
print("Number of vertices: ", number_of_vertices)
for i in range(number_of_vertices):
    f.write(str(i))
    if i != number_of_vertices-1:        
        f.write(",")  
f.write("\n")       

# get random max degree
max_degree = random.randint(1, number_of_vertices-1)

# random number of edges for each vertex
edges = []
for i in range(number_of_vertices):
    number_of_edges = random.randint(1, max_degree)
    for j in range(number_of_edges):
        edge = []
        startpoint = i
        endpoint = random.randint(1, number_of_vertices-1)
        while startpoint == endpoint:
            endpoint = random.randint(1, number_of_vertices-1)
        edge.append(startpoint)
        edge.append(endpoint)
        ce = []
        ce.append(endpoint)
        ce.append(startpoint)
        same_edge_found = False
        for test in edges:
            if test == edge or test == ce:
                same_edge_found = True
        if same_edge_found == False:
            edges.append(edge)

for edge in edges:
    f.write(str(edge[0]))
    f.write(",")
    f.write(str(edge[1]))
    f.write(";")
     