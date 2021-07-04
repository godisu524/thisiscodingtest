from collections import deque
def solution(grid):
    answer = 0
    n = len(grid)
    m = len(grid[0])
    
    dp = [] 
    dx =[0,1]
    dy =[1,0]
    
    dp.append([[0,0,grid[0][0]]])
    task = deque()
    task.append([dp[0][0]])
    while task:
        d = task.pop()
        for k in range(2):
            kx = dx[k] +d[-1][0]
            ky = dy[k] +d[-1][1]
            

            if kx< n and ky <m:
            
                temp = d.copy()
                temp.append([kx,ky,grid[kx][ky]])
                dp.append(temp)
                task.append(temp)
    ans=[]
    
    for d in dp:
        
        if d[-1][0]==n-1 and d[-1][1] == m-1:
            temp_sum = 0
            
            for num in d:

                temp_sum += num[-1]
            ans.append(temp_sum)
            

    return min(ans)

print(solution([[1, 8, 3, 2], [7, 4, 6, 5]]
))