import heapq



#매트릭스를 90% 회전시켜주는 코드
def rotate_a_matrix_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0]* n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i -1] = a[i][j]
    return result

# 전체돌면서 확인
def check(new_lock):
    lock_length = len(new_lock) //3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True


#문자가 알파벳인지
string = "???"
if string.isalpha():
    print("yes")