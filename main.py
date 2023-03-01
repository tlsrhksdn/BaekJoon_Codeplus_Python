def dfs():
  if len(s) == m:
    print(' '.join(map(str, s)))

  for i in range(n):
    if i not in s:
      s.append()
      dfs()
      s.pop()

n, m, k = map(int, input().split())

matrix = []

for i in range(n):
  for j in range(m):
    matrix[i][j] = 
s = []

dfs()
