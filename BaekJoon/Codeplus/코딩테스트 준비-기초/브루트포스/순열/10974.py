def dfs():
  if len(permutation) == n:    
    print(' '.join(map(str, permutation)))
    return

  for i in range(1, n+1):
    if i not in permutation:
      permutation.append(i)
      dfs()
      permutation.pop()
    
n = int(input())
permutation = []

dfs()



  
