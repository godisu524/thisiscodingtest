from itertools import permutations


def solution (k, dunjeons) :
    max =0
    answer = -1
    for trials in permutations(dunjeons,len(dunjeons)):
        life = k
        count =0 
        for dunjeon in trials:
            if dunjeon[0] <= life: 
                life -= dunjeon[1]
                count +=1
            else:
                break
        if max <= count:
            max = count
    
            







    return max




print(solution(80,[[80,20],[50,40],[30,10]]))