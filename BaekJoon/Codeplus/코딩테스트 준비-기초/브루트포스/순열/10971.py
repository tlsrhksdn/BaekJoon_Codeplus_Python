n = int(input())
matrix = [list(map(int, input().split()) for _  in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

min_ans = float('inf')

def back_tracking(depth, row, col):
  global min_ans
  route = []
  
  if depth == n :
    ans = 0
    for i in route:
      ans += i
    min_ans = min(min_ans, ans)

  for i in range(n):
    for j in range(n):
      if not visited[i][j]:
        visited[i][j] = True
        route.append(matrix[i][j])
        back_tracking(depth + 1, j, )
        visited[i][j] = False
        route.pop()
        
  

