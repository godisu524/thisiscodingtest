from collections import deque
n,k = map(int,input().split())
array= []
data = []
for i in range(n):
    array.append(list(map(int,input().split())))
    for j in range(n):
        if array[i][j] != 0:
            data.append((array[i][j], 0, i , j))

data.sort()
q= deque(data)            

ts,tx,ty, = map(int,input().split())



dx=[0,0,-1,1]
dy = [-1,1,0,0]

while q:
    virus, s, x, y = q.popleft()
    if s == ts:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx and nx<n and ny>=0 and ny<n:
            if array[nx][ny] ==0:
                array[nx][ny] = virus
                q.append((virus, s+1, nx, ny))


print(array[tx-1][ty-1])            