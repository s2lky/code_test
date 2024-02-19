from collections import deque

def bfs(n, m, maze):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    need_visit = deque([(0, 0)])

    while need_visit:
        x, y = need_visit.popleft()

        if x == n - 1 and y == m - 1:
            return maze[x][y]
                
        for dx, dy in directions: 
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                need_visit.append((nx, ny))
                maze[nx][ny] = maze[x][y] + 1
                

n, m = map(int, input().split())
maze = []

for i in range(n):
    line = str(input())
    row = [int(char) for char in line]
    maze.append(row)
        
print(bfs(n, m, maze))