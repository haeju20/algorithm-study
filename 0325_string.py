def solution(word):
    alph = [False] * 26

    # unicode 계산해서 알파벳 찾기
    alph[ord(word[0] - ord('a'))] = True

    for i in range(1, len(word)):
        # 다른 알파벳 등장했는데
        if word[i - 1] != word[i]:
            # 이미 등장했던 알파벳이라면 False
            if alph[ord(word[i]) - ord('a')]:
                return False
            alph[ord(word[i]) - ord('a')] = True
    return True

n = int(input())
result = 0
for _ in range(n):
    word = input().strip() # 공백 제거

    if solution(word):
        result += 1

print(result)
