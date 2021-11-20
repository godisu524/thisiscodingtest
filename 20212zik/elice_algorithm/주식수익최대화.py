
def maximizeProfit(nums):
    dp = [0]
    _max = 0
    _min = nums[0]
    for num in nums:
        profit = num - _min
        if profit > _max:
            _max = profit
        if num < _min:
            _min = num
            
        
    return _max

def main():
    print(maximizeProfit([1,2,3,4,5,6,7])) # 6
    print(maximizeProfit([7,6,5,4,3,2,1])) # 0
    print(maximizeProfit([1,2,3,4,3,2,1])) # 3
    print(maximizeProfit([2,8,19,37,4,5])) # 35

if __name__ == "__main__":
    main()