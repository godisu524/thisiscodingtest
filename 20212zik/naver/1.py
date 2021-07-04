def solution(lottery):
    answer = -1
    lot_dic = {}
    visited= []
    _sum = []
    for person in lottery:
        if person[0] not in lot_dic and person[0] not in visited:
            if person[1] == 1:
                lot_dic[person[0]] = [True]
                _sum.append(len(lot_dic[person[0]]))
                visited.append(person[0])
            else:
                lot_dic[person[0]] = [False]
        else:
            if person[0] == 1:
                lot_dic[person[0]].append(True)
                _sum.append(len(lot_dic[person[0]]))
                visited.append(person[0])
            else:
                lot_dic[person[0]].append(False)
    
    
    
    return sum(_sum) // len(_sum)
        
        
    
    
print(solution([[1, 0], [35, 0], [1, 0], [100, 1], [35, 1], [100, 1], [35, 0], [1, 1], [1, 1]]))