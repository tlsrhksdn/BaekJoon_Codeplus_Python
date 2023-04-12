numbers = list(input())

result = int(numbers[0])

for i in range(1, len(numbers)):
  temp = int(numbers[i])
  if temp <= 1:
    result = result + temp
  else:
    result = result * temp

print(result)
