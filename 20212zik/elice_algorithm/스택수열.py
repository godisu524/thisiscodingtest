def isStackSequence(nums):
    
    num_list = [i for i in range(1,len(nums)+1)]
    stack = []
    for num in num_list:
        stack.append(num)
        
        while nums[0] == stack[-1]:
            #print(stack)
            #print(nums)
            stack.pop()
            nums.pop(0)
            if len(stack) == 0:
                break
    #print(nums)
    if len(nums) == 0:
        return True
    else:
        return False
    

def main():
    #print(isStackSequence([2, 1, 4, 3])) # True가 리턴되어야 합니다
    print(isStackSequence([3, 1, 2, 4])) # False가 리턴되어야 합니다

    
if __name__ == "__main__":
    main()