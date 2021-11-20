from itertools import cycle

def solution(answers):
    answer = []
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    one_c = cycle(one)
    two_c = cycle(two)
    three_c = cycle(three)
    count_one = 0
    count_two = 0
    count_three = 0
    for ans in answers:
        if ans == next(one_c):
            count_one += 1
        if ans == next(two_c):
            count_two +=1
        if ans == next(three_c):
            count_three += 1    
    counts = [count_one,count_two,count_three]
    if counts.count(max(counts)) == 1:
        answer.append(counts.index(max(counts))+1)
    else:
        for i,c in enumerate(counts):
            if c == max(counts):
                answer.append(i+1)
        
        
    
            
    
    
    return answer