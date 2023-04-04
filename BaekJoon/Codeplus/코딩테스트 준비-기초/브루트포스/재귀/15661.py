import sys

N = int(sys.stdin.readline())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [False for _ in range(N)]
min_value = sys.maxsize

def backTraking(depth, idx):
  global min_value

  if depth == N//2:
    start, link = 0, 0
    for i in range(N):
      for j in range(i + 1, N):
        if visited[i] and visited[j]:
          start += S[i][j]
        elif not visited[i] and visited[j]:
          link += S[i][j]

    min_value = min(min_value, abs(start - link))
    return

    for i in range(idx, n):
      
    
    

backTracking(0, 0)
print(min_value)