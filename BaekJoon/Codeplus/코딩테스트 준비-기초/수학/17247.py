#1st try.failed
N = int(input())
sum = 0
for i in range(1, N + 1):
  numbers = map(int, input().split())
  for j in range(1, i + 1):
    if i % j == 0:
      numbers.append(j)
  for num in numbers:
    sum += num

print(sum)

#2nd try.Success

N = int(input())
sum = 0
for i in range(1, N+1):
  sum +=  i *  (N//i)

print(sum)