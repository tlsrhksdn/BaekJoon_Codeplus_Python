# 주어진 행렬을 생성할 수 있는 -10에서 10 사이의 정수들의 집합을 찾아라.
def check(idx):
  
  
def backtracking(idx):
  if idx == n:
    
    return


  for i in range(n):
    if visited[i]:
      
    
    

  


n = int(input())

container = list(input())

matrix = [[None for _ in range(n)] for _ in range(n)]
visited = [False for _ in range(10)]

# print(container)
    
for i in range(n):
  for j in range(i, n):
    matrix[i][j] = container.pop(-1)


#for i in range(n):
#  for j in range(n):
#    print(matrix[i][j])
    