n = int(input())
moves = list(input().split())


start =[1,1]
while moves:
    move = moves.pop(0)
    if move == "R" and start[1] <5:
        start [1]+=1
    elif move == "U" and start[0] >1:
        start[0]-=1
    elif move == "D" and start[0] <5:
        start[0]+=1
    elif move == "L" and start[0] >1:
        start[1]-=1

print(start)