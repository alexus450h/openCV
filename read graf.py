graph={i:set() for i in range(14)}
with open('d:/graph.txt', 'r') as file:
    for el in graph:
        graph[el]=file.readline().split()



print(graph)