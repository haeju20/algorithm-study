# 14500 (백준)
def dfs(x, y, step, total):
    global answer
    if total + max_val*(4-step) <= answer:
        return

    if step == 4:
        answer = max(answer, total)
        return

    for dx, dy in d:
        nx = x + dx
        ny = y + dy

        # 새 좌표가 n x m 내부에 있고 and 방문되지 않았으면
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if step == 2: # ㅜ
                visited[nx][ny] = True
                dfs(x, y, step+1, total+board[nx][ny])
                visited[nx][ny] = False

            visited[nx][ny] = True
            dfs(nx, ny, step+1, total+board[nx][ny])
            visited[nx][ny] = False

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
max_val = max(map(max, board)) # 각 행에서 max값 추출, 다시 max값 추출
d = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 좌, 우, 상, 하
visited = [[False] * m for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False # 방문했으니까 f

print(answer)
