def check(ans):
  vo, co = 0, 0
  
  for i in range(L):
    if ans[i] in vowels:
      vo += 1
    else:
      co += 1

  if vo >= 1 and co >= 2:
    return True
  else:
    return False
      
def password(idx):
  if len(ans) == L:
    if check(ans):
      print(' '.join(map(str, ans)))
    return
  
  for i in range(idx, C): 
    ans.append(words[i])
    password(i + 1)
    ans.pop()
    
  
L,C = map(int, input().split())

words = list(map(str, input().split()))

words.sort()

vowels = ['a','e','i','o','u']

ans = []

password(0)