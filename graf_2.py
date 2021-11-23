n,m=13,12
graf={
    0:{1,2,7,10},
    1:{3,4},
    2:{5,6},
    3:{1},
    4:{1},
    5:{2},
    6:{2},
    7:{8,9},
    8:{7},
    9:{7},
    10:{11},
    11:{10,12},
    12:{11}
}
start=0
distance=[None]*n
distance[start]=0
from  collections import deque
que=deque([start])
while que:
    cur_node=que.popleft()
    for neibor in graf[cur_node]:
        if distance[neibor]is None:
            distance[neibor]=distance[cur_node]+1
            que.append(neibor)
print(distance)
