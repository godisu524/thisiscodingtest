from collections import deque

n,m = map(int,input().split())
array=[]
for _ in range(n):
    array.append(list(map(int, input())))


dx = [1,-1,0,0]
dy = [0,0, 1,-1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            kx = x + dx[i]
            ky = y + dy[i]
            if kx<0 or ky<0 or kx>=n or ky >=m:
                continue
            if array[kx][ky] == 0:
                continue
            if array[kx][ky] == 1:
                array[kx][ky] =array[x][y]+1
                queue.append((kx,ky))
    return array[n-1][m-1]
print(bfs(0,0))



q=[[1,1]]










