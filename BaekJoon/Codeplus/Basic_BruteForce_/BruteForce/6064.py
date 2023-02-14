T = int(input())


for i in range(T):
  M, N, x, y = map(int, input().split())

  cnt = 0

  x_ = 0
  y_ = 0

  while True:
    
    if(x > y and M < N and x - y > N - M):
      print(-1)
      break
      
    elif(x < y and M > N and y - x > M - N):
      print(-1)
      break       
      
    else:
      if(x_ == x and y_ == y):
        print(cnt)
        break
      else:
    
        x_ += 1
        y_ += 1
        cnt += 1

        if x_ >= M:
          x_ %= M
        elif y_ >= N:
          y_ %= N

        

      
    