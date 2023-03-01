def dfs(start):
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for i in range(start, n):
    s.append(numbers[i])
    dfs(i)
    s.pop()


n, m = map(int, input().split())
s = []
numbers = list(map(int, input().split()))

numbers.sort()

dfs(0)