# 시간초과 에러 코드

def backtracking(depth, idx):
  global min_ans
  
  if depth == n//2:
    start, link = 0, 0

    for i in range(n):
      for j in range(n):        
        if visited[i] and visited[j]:
          start += (s[i][j] + s[j][i])
        elif not visited[i] and not visited[j]:
          link += (s[i][j] + s[j][i])

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

# 정답 코드
# 참고 블로그 : https://wlstyql.tistory.com/170

import sys
N = int(sys.stdin.readline())
_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [False] * N
result = []
_min = 1e9

def diff():
    _start = 0
    _link = 0
    # 오름차순 비교 for문으로 시간 절약
    for i in range(N-1):
        for j in range(i+1, N):
            # True인 경우 _start팀
            if visited[i] and visited[j]:
                _start += _map[i][j]  # S(i,j)
                _start += _map[j][i]  # S(j,i)
            # False인 경우 _link팀
            elif not visited[i] and not visited[j]:
                _link += _map[i][j]
                _link += _map[j][i]
    return abs(_start - _link)

def dfs(depth, idx, N):
    global _min
    if depth == N // 2:  # 절반만 선택
        diff_result = diff()
        _min = min(_min, diff_result)
        if _min == 0:  # 0이면 바로 출력
            print(_min)
            exit(0)
        return
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1, N)
            visited[i] = False
    return

dfs(0, 0, N)
print(_min)

# 문제 조건에서 j는 i보다 크거나 같아야 했으므로 