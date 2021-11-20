import queue

def josephus(num, target):
    nums = [i for i in range(1,num+1)]
    ans = []
    count=1
    while nums:
        if count != target:
            nums.append(nums.pop(0))
            count+=1
        else:
            ans.append(nums.pop(0))
            count=1 
    return ans

def main():
    print(josephus(7, 3)) #[3, 6, 2, 7, 5, 1, 4]이 반환되어야 합니다


if __name__ == "__main__":
    main()