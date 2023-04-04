def backtracking(depth, idx):
  global min_ans
  
  if depth == n//2:
    start, link = 0, 0

    for i in range(n):
      for j in range(n):        
        if visited[i] and visited[j]:
          start += s[i][j]
        elif not visited[i] and not visited[j]:
          link += s[i][j]

        min_ans = min(min_ans, abs(start - link))      
        
  for i in range(idx, n):
    if not visited[i]:
      visited[i] = True
      backtracking(depth + 1, idx + 1)
      visited[i] = False      
    
import sys
n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

min_ans = sys.maxsize
visited = [False for _ in range(n)]


backtracking(0, 0)
print(min_ans)