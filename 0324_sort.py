# 11399 (백준)
import sys

def solution(n, p):
    result = 0
    p.sort() # 오름차순 정렬
    for i in range(n):
        # 서로 역순으로 곱 (대기 시간 최소)
        result += p[i] * (n-i)
    return result

n = int(input())
p = [*map(int, input().split())]

print(solution(n, p))
