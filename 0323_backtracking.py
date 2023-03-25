# 9663 (백준)
def backtrack(r, n, is_queen_in_col, is_queen_in_left, is_queen_in_right):
    if r == n: # 모두 놓이면
        return 1

    cnt = 0

    for c in range(n):
        # 세로, 좌하향, 우하향 대각선에 퀸 없으면
        if not is_queen_in_col[c] and not is_queen_in_left[r+c] and not is_queen_in_right[r-c+n]:
            is_queen_in_col[c] = True
            is_queen_in_left[r+c] = True
            is_queen_in_right[r-c+n] = True

            # 다음 행에서 실행
            cnt += backtrack(r+1, n, is_queen_in_col, is_queen_in_left, is_queen_in_right)

            # 회수
            is_queen_in_col[c] = False
            is_queen_in_left[r+c] = False
            is_queen_in_right[r-c+n] = False

    return cnt

def solution(n):
    SIZE = 14

    is_queen_in_col = [False] * SIZE
    is_queen_in_left = [False] * (SIZE*2)
    is_queen_in_right = [False] * (SIZE*3)

    result = backtrack(0, n, is_queen_in_col, is_queen_in_left, is_queen_in_right)

    return result

n = int(input())
print(solution(n))
