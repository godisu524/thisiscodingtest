    

def findDuplicate(nums):
    
    nums.sort()
    for i in range(1,len(nums)):
        
        if i != nums[i-1]:
            
            return nums[i-1]
        
    
    
    
    
        
    

def main():
    print(findDuplicate([1, 5, 2, 4, 5, 6, 3]))

if __name__ == "__main__":
    main()