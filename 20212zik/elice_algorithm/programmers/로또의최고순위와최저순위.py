def solution(lottos, win_nums):
    answer = []
    count=7
    for num in win_nums:
        if num in lottos: 
            lottos.remove(num)
            count -=1
    if count == 7:
        worse = 6
    else:
        worse = count
    count = count - lottos.count(0)
    if count ==7:
        best = 6
    else:
        best = count
    
    answer = [best,worse]
    
    
    return answer