n,m = map(int,input().split())
array = list(map(int,input().split()))
result=0
def b_s(array,target,start,end):
    
    global result
    print(start,end,result)
    if start > end:
        return result
    total=0
    mid = (start+end)//2
    for x in array:
        if x >mid:
            total+=x-mid
    if total<target:
        return b_s(array,target,start,mid-1)
    else:
        result = mid
        return b_s(array,target,mid+1,end)



end = max(array)
answer =b_s(array, m, 0, end)
print(answer)
