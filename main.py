def count_candy():
  row_cnt, col_cnt, row_max, col_max = 1, 1, -1e9, -1e9
  # 행 계산
  for i in range(n):
    for j in range(n-1):
      if(board[i][j] == board[i][j+1]):
        row_cnt += 1
      else:
        row_cnt = 1
      row_max = max(row_cnt, row_max)
    row_cnt = 1
  #열 계산
  for j in range(n):
    for i in range(n-1):
      if board[i][j] == board[i+1][j]:
        col_cnt += 1
      else:
        col_cnt = 1
        
      col_max = max(col_cnt, col_max)
    col_cnt = 1
  answer = max(row_max, col_max)
  return answer

ans = 0

n = int(input())
board = [list(input()) for _ in range(n)]
steps = [[-1,0], [1,0], [0,-1], [0,1]]

for i in range(n):
  for j in range(n):
    for k in range(4):
      nx = i + steps[k][0]
      ny = j + steps[k][1]

      if nx<0 or nx >=n or ny < 0 or ny >= n:
        continue
      if board[i][j] != board[nx][ny]:
        board[nx][ny], board[i][j] = board[i][j], board[nx][ny]
        ans = max(ans, count_candy())
        board[i][j], board[nx][ny] = board[nx][ny], board[i][j]

print(ans)

        




        