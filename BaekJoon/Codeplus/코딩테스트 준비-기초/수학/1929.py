max = 1000000

dp = [1] * (max + 1)

for i in range(2, max + 1):
    j = 1
    while(i * j <= max):
      dp[i*j] += 1
      j += 1
            
while true:
    try:
        n = int(input())
        
    except:
    a=0
    b=0
    
    for i in range(3,n):
        if dp[i] == 2:
            a = i
    
    print("{%d} = {%d} + {%d}".format(n,a,n-a))