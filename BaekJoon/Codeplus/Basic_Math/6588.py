#1st try. fail

max = 1000000

dp = [1] * (max + 1)

for i in range(2, max + 1):
    j = 1
    while(i * j <= max):
        dp[i*j] += 1
        j += 1
            
while True:
    try:
        n = int(input())
        
    except:
      break
      
    a = 0
          
    for i in range(3,n):
        if dp[i] == 2:
            a = i
            break
    
    print(f'{n} = {a} + {n-a}')

#2nd try

array = [True for i in range(1000001)]

for i in range(2, 1001):
  if array[i]:
    for j in range(i + i, 1000001, i):
      array[j] = False

while True:
  try:
    n = int(input())

  except:
    break
  
  a = 0

  for i in range(3, n):
    if array[i] and array[n - i]:
      a = i
      break

  print(f'{n} = {a} + {n - a}')
      