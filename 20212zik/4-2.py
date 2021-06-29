n = int(input())

threes=[]
for i in range (60):
    if "3" in str(i):
        threes.append(i)
print(threes)

answer=0
for i in range(n+1):
    if "3" in str(i):
        answer+=3600
        continue
    for j in range(60):
        if j in threes:
            answer+=60
        else:
            answer+=len(threes)
print(answer)
#for i in range(n):
