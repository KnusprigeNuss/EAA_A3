This is my solution for A3 bonus.<br>
For the implementation I used Python 3.10.12<br>
g1 is just simple testcases which I used to test my implementation on a small scale and can be ignored<br>
<br>
How to run:<br>
1 - run the "create_graph.py" in order to randomly generate a graph<br>
2 - run the "graph_coloring.py" to get a coloring for the random graph<br>
<br>
Explanations:<br>
create_graph.py: This file creates a graph with a random amount of vertices in our case 10 and 300 (numbers can be changed but it was said "a few hundred" in the assignment sheet). Then it will randomly choose a max degree number. Then it will, for every vertex, create a random amount of edges between 1 and max degree to a random end vertex and add it to the edges list. Duplicates will not occur, I took care of that. The vertices and edges will then be written to "random_graph.txt".<br>
The syntax for that is as follows:<br>
<br>
0,1,2,3,4,5<br>
0,3;3,5;3,1;3,4;1,2;3,2;<br>
<br>
NOTE: its important that the file ends with a ";"<br>
<br>
<br>
graph_coloring.py: This file reads the contents from "random_graph.txt" (can be changed for manual testcases).<br>
Test output:<br>
<br>
Vertices:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]<br>
Edges:  [[0, 3], [3, 5], [3, 1], [3, 4], [1, 2], [3, 2], [5, 6], [6, 4], [2, 8], [4, 8], [6, 7], [7, 8], [8, 9]]<br>
Maximum degree:  5<br>
Colouring:  [3, 0, 4, 2, 5, 0, 1, 4, 2, 3]<br>
The computed colouring is correct!<br>
<br>
Vertices shows the number of vertices id's<br>
Edges shows between which points edges exist, each subarray is an edge<br>
Maximum degree is the maximum degree of the graph<br>
Colouring shows the id of the color each vertex has to get<br>
NOTE: array index for vertices and colouring are the same (for the above example the first vertex 0 has to get colour 3)<br>
The last line checks for each edge once again if the start and end point really don't have the same color and outputs a prompt<br>
<br>
Please excuse the loading times with big number of vertices it is python after all.<br>