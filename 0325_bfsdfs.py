# 2638
import sys
sys.setrecursionlimit(10 ** 8)

board = []
dr = [-1, 1, 0, 0] # 좌, 우
dc = [0, 0, -1, 1] # 하, 상

def dfs(n, m, row, col):
    if row < 0 or row >= n or col < 0 or col >= or board[row][col] != 0:
        return
    board[row][col] = -1 # 외부 공기
    for i in range(4):
        dfs(n, m, row+dr[i], col+dc[i])

def canMelt(row, col):
    cnt = 0
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if board[nr][nc] == -1: # 외부 공기
            cnt += 1
    return cnt >= 2

def findCheese(n, m):
    cheese = list()
    for i in range(n):
        for j in range(m):
            # 치즈 and 녹을 수 있으면
            if board[i][j] == 1 and canMelt(i, j):
                cheese.append([i, j])
    return cheese

def solution(n, m, input_board):
    for i in range(n):
        board.append(input_board[i][:]) # shallow copy
    answer = 0
    dfs(n, m, 0, 0)
    while True:
        # 녹을 치즈들 찾기
        cheese = findCheese(n, m)
        if not cheese:
            break

        for a in cheese:
            row, col = a
            board[row][col] = 0
            dfs(n, m, row, col)
        answer += 1

    return answer

input = sys.stdin.readline
n, m = map(int, input().split())
input_board = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, m, input_board))
