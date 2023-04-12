n = int(input())

numbers = list(map(int, input().split()))
numbers.sort()

result = 0
count = 0

for i in numbers:
  count += 1
  if count >= i:
    result += 1
    count = 0

print(result)
