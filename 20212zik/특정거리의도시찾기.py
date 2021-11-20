n,m,k,x = map(int,input().split())
roads=[]
visited = [False for i in range(n+1)]
for _ in range(n+1):
    roads.append([])

for _ in range(m):
    start, end = map(int,input().split())
    roads[start].append(end)

q = [x]
count=0
while q:
    rounds= len(q)
    for _ in range(rounds):
        temp = q.pop(0)
        for road in roads[temp]:
            if visited[road] == False:
                q.append(road)
                visited[road] =  True
    count+=1
    if count ==k:
        if len(q) != 0:
            for road in sorted(q):
                print(road)
        else:
            print(-1)
        
    

    
