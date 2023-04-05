def compare(i, j, comp):
  if comp == ">":
    return i > j
  else:
    return i < j

def backtracking(depth, s):
  global min_ans, max_ans
  
  if depth == k+1:
    if len(min_ans) == 0:
      min_ans = s
    else:
      max_ans = s      
    return   
    
  for i in range(10):
    if not visited[i]:
      if (depth == 0 or compare(s[-1], str(i), inequalities[depth - 1])):
        visited[i] = True
        backtracking(depth + 1, s+str(i))
        visited[i] = False

k = int(input())
inequalities = list(input().split())
visited = [False]*10

min_ans, max_ans = "", ""

backtracking(0, "")
print(max_ans)
print(min_ans)






