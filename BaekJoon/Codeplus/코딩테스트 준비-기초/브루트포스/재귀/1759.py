# cnt는 문자개수, idx는 인덱스값
def password(cnt, idx):
  if cnt == 1:
    vo, co = 0, 0

    for i in range(L):
      if ans[i] in vowel:
        vo += 1
      else:
        co += 1
  
    if vo >= 1 and co >= 2:
      if len(ans) == L:
        
        print(' '.join(map(str, ans)))
        return
  
  for i in range(L):
    if words[i] not in ans:
      ans.append(words[i])
      password(cnt+1,idx)
      ans.pop()
    
  
L,C = map(int, input().split())

words = list(map(str, input().split()))

words.sort()

vowel = ['a','e','i','o','u']
ans = []

password(0,0)