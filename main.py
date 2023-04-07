def dfs_permutation(arr, n):
  ret = []
  idx = [i for i in range(len(arr))]

  stack = []
  for i in idx:
    stack.append(i)

  while len(stack) != 0:
    cur = stack.pop()

    for i in idx:
      if i not in cur:
        temp = cur + [i]
        if len(temp) == n:
          element = []
          for i in temp:
            element.append(arr[i])
          ret.append(element)
        else:
          stack.append(temp)
  return ret
  

n = int(input())

numbers = list(map(int, input().split()))


