
def moveZerosToEnd(nums):
    
    index=0
    
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[index] = nums[i]
            if i != index:
                nums[i] = 0
            index+=1
            
    
            
    return nums

def main():
    print(moveZerosToEnd([0, 8, 0, 37, 4, 5, 0, 50, 0, 34, 0, 0]))

if __name__ == "__main__":
    main()
