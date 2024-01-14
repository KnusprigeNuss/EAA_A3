import random
random.seed()


# read input file and convert to a graph
f = open("random_graph.txt", "r")
vertices = f.readline()
vertices = vertices[:-1]
new_vertex_list = vertices.split(',')
for i in range(len(new_vertex_list)):
    new_vertex_list[i] = int(new_vertex_list[i])
edges_array = []
edges = f.readline()
new_edge_list = edges.split(';')
new_edge_list.pop()
for i in range(len(new_edge_list)):
    test = new_edge_list[i].split(',')
    for j in range(len(test)):
        test[j] = int(test[j])
    edges_array.append(test)
graph = [new_vertex_list, edges_array]
print("Vertices: ", new_vertex_list)
print("Edges: ", edges_array)


# check for the max degree
max_degree = 0
for vertex in graph[0]:
    current_degree = 0
    for edge in graph[1]:
        if edge[0] == vertex or edge[1] == vertex:
            current_degree += 1
    if current_degree > max_degree:
        max_degree = current_degree
print("Maximum degree: ", max_degree)
new_colour_set = []
for i in range(max_degree+1):
    new_colour_set.append(i)


# coloring process
colouring = [-1] * len(new_vertex_list)
for vertex in graph[0]:
    v_colour = 0
    not_correct_colour = True
    while(not_correct_colour):
        v_colour = random.randint(0, max_degree)
        doomed = False
        for edge in graph[1]:
            if edge[0] == vertex:
                if colouring[edge[1]] == v_colour:
                    doomed = True
            if edge[1] == vertex:
                if colouring[edge[0]] == v_colour:
                    doomed = True
        if doomed == False:
            not_correct_colour = False
    colouring[vertex] = v_colour
print("colouring: ", colouring)


# checker
for edge in graph[1]:
    if colouring[edge[0]] == colouring[edge[1]]:
        print("The computed colouring is incorrect!")
        exit(-1)
print("The computed colouring is correct!")
        

