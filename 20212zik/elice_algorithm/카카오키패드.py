def solution(numbers, hand):
    answer = ''
    L = [1,4,7]
    M = [2,5,8,0]
    R = [3,6,9]
    keypad=[[1,2,3],[4,5,6],[7,8,9],["*",0,'#']]
    last_pos_L="*"
    last_pos_R="#"
    target = [-1,-1]
    target_L = [-1,-1]
    target_R = [-1,-1]
    for number in numbers:
        print("----------", last_pos_L,last_pos_R)
        if number in L:
            print(number,"L")
            last_pos_L = number
            answer+="L"
        elif number in R:
            print(number,"R")
            last_pos_R = number
            answer +="R"
        else:
            for n,keys in enumerate(keypad):
                if number in keys:
                    target=[n,keys.index(number)]
                if last_pos_L in keys:
                    target_L=[n,keys.index(last_pos_L)]
                if last_pos_R in keys:
                    target_R=[n,keys.index(last_pos_R)]
            if abs(target[0]-target_L[0])+abs(target[1]-target_L[1]) < abs(target[0]-target_R[0])+abs(target[1]-target_R[1]):
                print(target_R,target_L,target)
                print(number,"1L")
                last_pos_L = number
                answer+="L"
            elif abs(target[0]-target_L[0])+abs(target[1]-target_L[1]) > abs(target[0]-target_R[0])+abs(target[1]-target_R[1]):
                print(number,"2R")
                last_pos_R = number
                answer+="R"
            else:
                if hand =="right":
                    print(number,"3R")
                    last_pos_R = number
                    answer+="R"
                else:
                    print(number,"4L")
                    last_pos_L = number
                    answer+="L"
                    
            
    return answer

print(solution(	[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))