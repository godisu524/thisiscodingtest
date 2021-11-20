def solution(n, lost, reserve):

    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)

    
    for i in set_lost:
        if i-1 in set_reserve :
            set_lost.remove(i-1)
        elif i +1 in set_reserve:
            set_lost.remove(i+1)

        #print(lost, reserve)
    return n-len(set_lost)



print(solution(5, [2,3,4], [3, 4,5]	))