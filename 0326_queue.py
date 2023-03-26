import heapq

def insert(n, max_pq, min_pq, cnt):
    heapq.heappush(min_pq, n)
    heapq.heappush(max_pq, -n)
    if n not in cnt:
        cnt[n] = 0
    cnt[n] += 1

def deleteMax(max_pq, cnt):
    if max_pq:
        cnt[-max_pq[0]] -= 1
        if cnt[-max_pq[0]] == 0:
            del cnt[-max_pq[0]]
        heapq.heappop(max_pq)

def deleteMin(min_pq, cnt):
    if min_pq:
        cnt[min_pq[0]] -= 1
        if cnt[min_pq[0]] == 0:
            del cnt[min_pq[0]]
        heapq.heappop(min_pq)

def cleansPqs(max_pq, min_pq, cnt):
    while min_pq and min_pq[0] not in cnt:
        heapq.heappop(min_pq)
    while max_pq and -max_pq[0] not in cnt:
        heapq.heappop(max_pq)

def solution(operations):
    min_pq = []
    max_pq = []
    cnt = {} # 남아있는 i 개수

    for operation in operations:
        cmd = operation[0] # 명령어
        n = int(operation[2:]) # 데이터

        if cmd == 'I':
            insert(n, max_pq, min_pq, cnt)
        else:
            if n == 1:
                deleteMax(max_pq, cnt)
            else:
                deleteMin(min_pq, cnt)

            # 삭제된 값 동기화
            cleansPqs(max_pq, min_pq, cnt)
    cleansPqs(max_pq, min_pq, cnt)

    if not max_pq or not min_pq: # 비어있으면
        return [0, 0]
    else:
        return [-max_pq[0], min_pq[0]]
