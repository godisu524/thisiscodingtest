
def thirdMax(nums):
    #nums.sort()
    nums.remove(max(nums))
    nums.remove(max(nums))
    
    return max(nums)

def main():
    print(thirdMax([2, 8, 19, 37, 4, 5, 12, 50, 1, 34, 23])) # should return 34

if __name__ == "__main__":
    main()
