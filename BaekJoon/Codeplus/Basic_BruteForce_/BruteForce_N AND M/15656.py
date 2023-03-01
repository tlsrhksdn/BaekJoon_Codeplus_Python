def dfs():
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for i in range(n):
    s.append(numbers[i])
    dfs()
    s.pop()


n, m = map(int, input().split())
s = []
numbers = list(map(int, input().split()))

numbers.sort()

dfs()