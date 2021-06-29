move = str(input())

start=[0,0]
start[0] = ord(move[0]) - ord('a')+1
start[1]= int(move[1])

answer = 0
steps = [(1,2),(1,-2),(-1,-2),(-1,2),(2,1),(2,-1),(-2,1),(-2,-2)]

for step in steps:
    if start[0]+step[0] <=8 and start[0]+step[0] >=1 and start[1]+step[1] <=8 and start[1]+step[1] >=1 :
        answer +=1
    


print(answer)