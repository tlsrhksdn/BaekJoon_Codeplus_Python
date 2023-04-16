import sys

m = int(input())
s = set()

for i in range(m):
  temp = sys.stdin.readline().strip().split()

  if len(temp) == 1:
    if temp[0] == "all":
      s = set([i for i in range(1, 21)])
    else:
      s = set()
    continue
    
  command, target = temp[0], temp[1]
  target = int(target)

  if command == 'add':
    s.add(target)
  elif command == 'check':
    print(1 if target in s else 0)
  elif command == 'remove':
    s.discard(target)
  elif command == 'toggle':
    if target in s:
      s.discard(target)
    else:
      s.add(target)
      
