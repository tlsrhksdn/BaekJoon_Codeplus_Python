import sys
n = int(sys.stdin.readline())
graph = [ list(map(int, sys.stdin.readline().split())) for _ in range(n) ]
visited = [ False for _ in range(n) ] 
min_value = sys.maxsize 

def backTracking(depth, idx): 
    global min_value
    if depth == n // 2: 
        power1, power2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]: 
                    power1 += graph[i][j]
                elif not visited[i] and not visited[j]: 
                    power2 += graph[i][j]
        min_value = min(min_value, abs(power1-power2)) 
        return

    for i in range(idx, n): 
        if not visited[i]:
            visited[i] = True
            backTracking(depth + 1, idx + 1) 
            visited[i] = False
          
backTracking(0, 0)
print(min_value)

