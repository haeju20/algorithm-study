def calculate(n):
    dp = [[0, 0]] * (n+1)

    for i in range(2, n+1):
        # case 3
        # 언제나 가능한 조건이므로 case 3으로 초기화
        dp[i] = [dp[i-1][0] + 1, i - 1]

        # case 1
        # case 3 값과 비교해서 작을 때만 업데이트
        if(i % 3 == 0 and dp[i][0] > dp[i//3][0]):
            dp[i] = [dp[i//3][0] + 1, i//3]

        # case 2
        # case 3 값과 비교해서 작을 때만 업데이트
        if(i % 2 == 0 and dp[i][0] > dp[i//2][0]):
            dp[i] = [dp[i//2][0] + 1, i//2]

    return dp

def solution(n):
    dp = calculate(n)

    result = [0, []]
    result[0] = dp[n][0]
    temp = n

    # result[1]에 1로 만드는 방법에 포함된 수 append
    while temp != 0:
        result[1].append(temp)
        temp = dp[temp][1]

    return result

n = int(input())
result = solution(n)
print(result[0]) # 연산 횟수의 최솟값
print(*result[1]) # 1로 만드는 방법에 포함된 수
