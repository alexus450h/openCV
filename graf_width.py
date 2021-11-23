n,m=map(int,input('Inputs q Nods').split())
graph={i:set() for i in range(n)}
print(graph)
# for i in range(m):
#     v1,v2=map(int,input('coords').split())
#     graph[v1].add(v2)
#     graph[v2].add(v1)
graph={0: {1, 5, 8, 11},
 1: {0, 3},
 2: {0,3},
 3: {1, 4},
 4: {3},
 5: {0, 6},
 6: {5, 7},
 7: {6},
 8: {0, 9, 10},
 9: {8},
 10: {8},
 11: {0, 12, 13},
 12: {11},
 13: {11}}
from collections import deque
distance=[None]*n
start=0
distance[start]=0
que=deque([start])
print(que)
while que:
    cur_vert=que.popleft()
    for neibor  in graph[cur_vert]:
        if distance[ neibor]is None:
            distance[neibor]=distance[cur_vert]+1
            que.append(neibor)
print(distance)