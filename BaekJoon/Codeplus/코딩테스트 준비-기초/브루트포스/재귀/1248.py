# 행렬의 값이 양수면 +기호를 저장하고, 음수면 -기호를 저장한다


def backtracking(depth, idx):
  if depth == n :
    return
  return


n = int(input())

container = list(input())

matrix = [[None for _ in range(n)] for _ in range(n)]

for i in range(n):
  for j in range(i, n):
    matrix[i][j] = container.pop(-1)
    print(matrix[i][j])
