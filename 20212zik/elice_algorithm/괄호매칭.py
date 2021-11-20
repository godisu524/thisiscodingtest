returns = [")","]","}",">"]
insert = ["(","[","{","<"]
def isParenthesisValid(st):
    qq=[]
    for letter in st:
        if letter not in returns:
            qq.append(letter)   
        else:
            if len(qq) != 0:
                if insert.index(qq.pop()) == returns.index(letter):
                    continue
                else:
                    return False
            
    return True

def main():
    examples = ["({()})", "[]<>{}", ")(" "<]", "<(>)"]
    for example in examples:
        print(example, isParenthesisValid(example))

    
if __name__ == "__main__":
    main()