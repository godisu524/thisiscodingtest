import bisect
n, m = map(int, input().split())
#m = target
array= list(map(int,input().split()))
print(bisect.bisect_right(array,m)- bisect.bisect_left(array,m))


#bisect 를 통해 이진법을 통해 찾은 것의 왼쪽 오른쪽을 알 수 있음. 만약 한개면 오 !
