def solution(n,a,b):
    if a > b:
        temp = a
        a = b
        b= temp

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    #print('Hello Python')
    answer=0
    while True:
        answer+=1
        if b-a == 1 and b %2 ==0:
            return answer
        if a %2 != 0:
            a//=2
            a+=1
        else:
            a//=2
        if b%2 !=0:
            b //=2
            b+=1
        else:
            b//=2
        
        
        
    
    

print(solution(8,4,7))
