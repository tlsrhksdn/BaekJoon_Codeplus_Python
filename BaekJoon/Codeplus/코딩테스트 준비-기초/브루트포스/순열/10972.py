n = int(input())

numbers = list(map(int,input().split()))

for i in range(n):
  if numbers[i] < numbers[i+1]:
    for j in range(i+1, n):
      if numbers[i+1] < numbers[j]:
        numbers[i+1], numbers[j] = numbers[j], numbers[i+1]
    numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
  print(' ',map(str, numbers))
  
