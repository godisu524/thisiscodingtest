from typing import Deque
import copy

def solution(n, wires):
    real_wires = copy.deepcopy(wires)
    answer = 9999999999
    for i in range(len(real_wires)):
        
        cut_line = wires.pop(i)
        #print(wires)
        graph = [[] for _ in range(n+1)]
        total = []
        #making graph
        for wire in wires:
            graph[wire[0]].append(wire[1])
            graph[wire[1]].append(wire[0])
        for c in cut_line:
            count = 0
            visited = [c]
            q=Deque([c])
            while q: 
                print(q)
                count +=1
                temp = q.popleft()
                if len(graph[temp]) != 0:
                    for nodes in graph[temp]:
                        if nodes not in visited:
                            q.append(nodes)
                            visited.append(nodes)
            total.append(count)
        print(total)
        if abs(total[0]-total[1]) < answer:
            answer = abs(total[0]-total[1])
            print(answer)
        
        wires = copy.deepcopy(real_wires)
        
            

    


    


    return answer


print(solution(3, [[1,2],[2,3]] ))