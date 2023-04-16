def rotate_array(numbers,ch):
  ans = []

  if ch == '1':
    for i in range(n):
      for j in range(m):
        numbers[i][j], numbers[n-1-i][j] = numbers[n-1-i][j], numbers[i][j]

  if ch == '2':
    for i in range(n):
      for j in range(m):
        numbers[i][j], numbers[i][m-1-j] = numbers[i][m-1-j], numbers[i][j]
        
  if ch == '3':
    for i in range(n):
      for j in range(m):
        

        
    

n,m,r = map(int, input().split())

numbers = [list(map(int, input().split())) for _ in range(n)]

