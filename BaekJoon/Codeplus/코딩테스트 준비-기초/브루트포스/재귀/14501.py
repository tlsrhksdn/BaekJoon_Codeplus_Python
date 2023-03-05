# 틀린 코드

N = int(input())

time = [0]
money = [0]

dp = [0 for i in range(N+1)]

for i in range(1,N+1):
  T,P = map(int, input().split())
  time.append(T)
  money.append(P)

for i in range(1,N+1):
  for j in range(i + time[i], N+1):
    dp [j] = max(dp[j], dp[i] +money[i]) 

  print(dp)

print(dp[N])


# 코드상으로는 훨씬 깔끔하지만, 세 번째 테스트 케이스에서 오류 발생

# 1 + 5 + 5는 11이지만, 인덱스값은 10까지만 존재하므로 답을 출력하는 것이 불가능해짐

# 따라서 부득이하게 코드를 아래와 같이 수정함(N+1개의 인덱스를 가진 배열을 생성해줌으로써 해결 가능)

# 정답

N = int(input())

time = [0 for i in range(N+2)]
money = [0 for i in range(N+2)]

dp = [0 for i in range(N+2)]

for i in range(1,N+1):
  T,P = map(int, input().split())
  time[i] = T
  money[i] = P

for i in range(1,N+2):
  for j in range(i + time[i], N+2):
    dp [j] = max(dp[j], dp[i] +money[i]) 

  print(dp)

print(dp[N+1])