#1st ans. fail
'''
T = int(input())

for test in range(T):
  
  N = int(input())
  sum = 0
  for i in range(1, N+1):
    sum +=  i *  (N//i)
  
  print(sum)

'''

#2nd ans. fail
max = 1000000

dp = [1] * (max+1)
s = [0] * (max+1)

for i in range(2, max+1):
  j  = 1
  while(i * j <= max):
    dp[i*j] += i
    j += 1

for i in range(1, max+1):
  s[i] = s[i-1] + dp[i] 

T = int(input())
ans = []

for i in range(T):
  N = int(input())

  print(ans[N])
  
  

#3rd ans. success

max = 1000000

dp = [1] * (max+1)
s = [0] * (max+1)

for i in range(1, max+1):
  j  = 1
  while(i * j <= max):
    dp[i*j] += i
    j += 1
    s[i] = s[i-1] + dp[i] 
      

T = int(input())
ans = []

for i in range(T):
  N = int(input())
  ans.append(s[N])

print('\n'.join(map(str,ans)))