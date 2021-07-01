n,m = map(int,(input().split()))
answer= 0
start = list(map(int,input().split()))

array =[]
for i in range(n):
    array.append(list(map(int,input().split())))

visited = [[False for _ in range(n)] for _ in range(m)]

moves = [[-1,0],[0,1],[1,0],[0,-1]]

player = start


print(player)
visited[player[0]][player[1]] = True
while True:
    m_count =4 
    temp_answer = answer
    for v in visited:
        print(v)
    print()    
    while(m_count!=0):
        #print(player[2])
        nx, ny = moves[player[2]][0], moves[player[2]][1]
        
        kx = player[0]+nx
        ky = player[1]+ny



        if 0<=kx and kx <n and ky >=0 and ky <m:
            if not visited[kx][ky]  and array[kx][ky] != 1:
                player[0] = kx
                player[1] = ky
                answer +=1
                visited[player[0]][player[1]] = True
                if player[2] == 0:
                    player[2] = 3
                else:
                    player[2] -=1
                break
        m_count -=1
        if player[2] == 0:
            player[2] = 3
        else:
            player[2] -=1
    if temp_answer == answer:
        break
print(answer+1)


