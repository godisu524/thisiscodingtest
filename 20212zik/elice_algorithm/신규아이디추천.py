import re

def solution(new_id):
    answer = ''
    #1단계
    new_id = new_id.lower()
    #print("1", new_id)
    #2단계
    p = re.compile("[^0-9a-zA-Z-_.]")
    new_id = p.sub("",new_id)
    #print("2", new_id)
    #3단계
    while ".." in new_id:
        new_id = new_id.replace("..", ".")
    #print("3", new_id)
    #4단계
    if new_id.startswith("."):
        new_id = new_id[1:]
    if new_id.endswith("."):
        new_id = new_id[:-1]
    #print("4", new_id)
    #5단계
    if len(new_id) == 0:
        new_id = "a"
    #print("5", new_id)
    #6단계
    if len(new_id)>15:
        new_id = new_id[:15]
        if new_id.endswith("."):
            new_id = new_id[:-1]
    #print("6", new_id)
    #7단계
    while len(new_id)< 3:
        new_id+=new_id[-1]
    #print("7", new_id)
    return new_id


print(solution("...!@BaT#*..y.abcdefghijklm"))