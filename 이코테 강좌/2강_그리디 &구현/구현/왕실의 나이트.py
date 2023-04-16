# 문제 세팅
position = input()

row = int(position[1])
column = int(ord(position[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2,1)]

result = 0

# 이하 구현
#...