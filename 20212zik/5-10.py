n,m = map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,(input()))))

visited=[[False]*n for _ in range(m)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x,y):
    if x <=-1 or x>=n or y<= -1 or y >=m:
        return False
    if graph[x][y]==0:
        graph[x][y]= 1
        for k in range(4):
            dfs(x+dx[k], y+dy[k])
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result +=1
print(result)
