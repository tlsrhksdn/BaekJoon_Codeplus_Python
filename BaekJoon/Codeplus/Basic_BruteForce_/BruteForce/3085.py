def count_candy():
  row_cnt, col_cnt, row_max, col_max = 1, 1, -1e9, -1e9
  # 행 계산
  for i in range(n):
    for j in range(n-1):

  #열 계산
  for j in range(n):
    for i in range(n-1):
  
      
  answer = max(row_max, col_max)
  return answer

ans = 0

n = int(input())
board = [list(input()) for _ in range(n)]
steps = [[-1,0], [1,0], [0,-1], [0,1]]

for i in range(n):
  for j in range(n):
    for k in range(4):

print(ans)
        
        
        




        