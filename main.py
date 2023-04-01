N = int(input())

time = [0]
money = [0]

dp = [0 for i in range(N+1)]

for i in range(N):
  T,P = map(int, input().split())
  time.append(T)
  money.append(P)

for i in range(N):
  for j in range(i + time[i], N+1):
    dp [j] = max(dp[j], dp[i] +money[i]) 

  print(dp)

print(dp[N])