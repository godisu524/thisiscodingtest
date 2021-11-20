def binary_search(array, target, start, end):
    if start> end:
        return None
    mid = (start+end)//2
    #찾은 경우 인덱스 반환
    if array[mid] == target:
        return mid
    #중간값보다 찾고자 하는 값이 작은 경우 안쪽 확인
    elif array[mid] >= target:
        return binary_search(array,target, start, mid-1)
    #중간값보다 찾고자하는 값이 큰경우 오른쪽 확인
    else:
        return binary_search(array, target, mid+1, end)
    

n,target= list(map(int,input().split()))
array = list(map(int, input().split()))
result = binary_search(array,target,0,n-1)
if result == None:
    print("nono")
else:
    print(result+1)


