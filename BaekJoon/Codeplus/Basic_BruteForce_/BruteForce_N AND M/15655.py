def dfs():
  if len(s) == m:
    print(' '.join(map(str, s)))
    return 

  for i in range(n):
    if numbers[i] not in s:
      s.append(numbers[i])
      dfs()
      s.pop()


n, m = map(int, input().split())
numbers = list(map(int, input().split()))
s = []

dfs()



