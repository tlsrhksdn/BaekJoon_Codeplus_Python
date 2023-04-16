array = list(input())

characters = []
value = 0

for ch in array:
  if ch.isalpha():
    characters.append(ch)
  else:
    value += int(ch)

characters.sort()

if value != 0:
  characters.append(value)

print(''.join(characters))

