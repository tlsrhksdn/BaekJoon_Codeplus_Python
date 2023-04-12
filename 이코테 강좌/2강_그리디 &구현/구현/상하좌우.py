# 첫 번째 코드

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

x, y = 1, 1

n = int(input())

directions = input().split()

def move_to_direction(ch):
  if ch == 'L':
    x = x + dx[0]
    y = y + dy[0]
  elif ch == 'R':
    x = x + dx[1]
    y = y + dy[1]
  elif ch == 'U':
    x = x + dx[2]
    y = y + dy[2]
  elif ch == 'D':
    x = x + dx[3]
    y = y + dy[3]

for i in directions:
  move_to_direction(i)

print(x)


# 수정

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

x, y = 1, 1

n = int(input())

directions = input().split()

# 이하동일

# 움직이는 방향을 리스트에 저장
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인하기
for plan in plans:
  # 이동 후 좌표 구하기 
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  #공간을 벗어나는 경우 무시
  if nx < i or ny < i or nx > n or ny > n:
    continue

  x, y = nx, ny

print(x, y)
  