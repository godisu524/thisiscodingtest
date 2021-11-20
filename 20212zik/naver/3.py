def solution(arr, k):
    length = len(arr) - 1
    answer=0
    _nums = [i for i in range(k+1)]
    _nums.reverse()
    _nums.pop()
    #차이가 큰게 갈길이 머니까 차이큰거부터 하자.
    sorted_arr = sorted(arr)
    while sorted_arr != arr:
        print(arr)
        temps= []
        for i in range(length):
        
            for j in range(length-i):
                for kk in _nums:
                    if j+kk <= length:
                        if arr[j] > arr[j+kk]:   
                            temps.append([j,j+kk,max(abs((j+kk)-sorted_arr.index(arr[j])),abs((j)-sorted_arr.index(arr[j+kk])))])
        temps.sort(key = lambda x: x[2])
        #print(temps)
        if temps:
            arr[temps[-1][0]], arr[temps[-1][1]] = arr[temps[-1][1]], arr[temps[-1][0]]
            answer+=1
        #arr[j], arr[j+kk] = arr[j+kk], arr[j]
                
        
            

    return answer


print(solution([5,4,3,2,1],	2))


