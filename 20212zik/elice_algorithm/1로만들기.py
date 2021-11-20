
def convertTo1(num):
    dp =[0]
    dp.append(0)
    dp.append(1)
    dp.append(1)
    
    target = 4
    while target<=num:
        
        ables=[]
        if target % 3 == 0:
            ables.append(dp[target//3])
        if target % 2 == 0:
            ables.append(dp[target//2])
        ables.append(dp[target-1])
        
        dp.append(min(ables)+1)                                            
        
        
        target+=1
    
    return dp[num]

def main():
    print(convertTo1(10))

if __name__ == "__main__":
    main()
