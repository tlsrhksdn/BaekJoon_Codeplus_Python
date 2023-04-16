n,m,x,y,k = map(int, input().split())

numbers = [list(map(int, input().split())) for _ in range(n)]

instructions = map(int, input().split())
 
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def move_direction(x, y, ch):
  if ch == '1':
    x = x + dx[0]
    y = y + dx[0]
    
  if ch == '2':
    x = x + dx[1]
    y = y + dx[1]

  if ch == '3':
    x = x + dx[2]
    y = y + dx[2] 

  if ch == '4':
    x = x + dx[3]
    y = y + dx[3]




