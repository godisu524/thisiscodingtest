def binary_search(array,target, start,end):
    if start > end:
        return None
    mid= (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)


n= int(input())
array_m = list(map(int,input().split()))
m = int(input())
array_n = list(map(int,input().split()))

array_m.sort()


answer = []
for num in array_n:
    if binary_search(array_m,num,0,len(array_m)) != None:
        answer.append("yes")
    else:
        answer.append("no")
print(answer)