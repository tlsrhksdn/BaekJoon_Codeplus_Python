n = int(input())
k = list(map(int, input().split()))

dp = [0] * 100
dp[1] = k[0]
dp[2] = max(k[0], k[1])

for i in range(3, n+1):
  dp[i] = max(dp[i-1], dp[i-2] + k[i-1])
  
print(d[n])