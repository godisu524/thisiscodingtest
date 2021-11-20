n= int(input())
foods = list(map(int,input().split()))

dp = [0 for _ in range(len(foods))]

dp[0] = foods[0]
dp[1] = max(dp[0], foods[1])

for k in range(2,len(foods)):
    dp[k] = max(dp[k-1], dp[k-2]+foods[k])


print(dp[n-1])