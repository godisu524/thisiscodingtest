def solution(scores):
    answer = ''
    ans_list=[[] for _ in range(len(scores))]
    for j in range(len(scores)):
        for i in range(len(scores[0])):
            ans_list[j].append(scores[i][j])
        if ans_list[j].index(max(ans_list[j])) == j or ans_list[j].index(min(ans_list[j])) == j :
                if ans_list[j].count(ans_list[j][j]) == 1:
                    ans_list[j].remove(ans_list[j][j])            
    for ans in ans_list:
        grade = sum(ans)/len(ans)
        #print(grade)
        if grade >= 90:
            answer+="A"
        elif grade >= 80:
            answer+="B"
        elif grade >= 70:
            answer+="C"
        elif grade >= 50:
            answer+="D"
        else:
            answer+="F"            
    print(ans_list)
    return answer

print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]	))