def solution(board, move):
    result = 0
    stack = []

    for i in range(len(move)):
        col = move[i] - 1
        for j in range(len(board)):
            if board[j][col] == 0: #인형 없으면
                continue

            # 인형 뽑고 초기화
            doll = board[j][col]
            board[j][col] = 0

            # 스택이 비어 있지 않고 and 뽑은 인형과 스택 위에 있는 인형이 같을 때
            if stack and doll == stack[-1]:
                stack.pop()
                result += 2
            else:
                stack.append(doll)
            break

    return result

board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
move = [1, 5, 3, 5, 1, 2, 1, 4]
print(solution(board, move))
