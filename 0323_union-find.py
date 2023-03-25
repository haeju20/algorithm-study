def Find(node, parent):
    if parent[node] == -1:
        return node
    return Find(parent[node], parent)

def Union(x, y, parent, knowsTruth):
    x = Find(x, parent)
    y = Find(y, parent)

    if x == y: # 파티에 한 사람만 참여
        return

    if knowsTruth[x]: # x만 알거나 둘 다 알 때
        parent[y] = x
    elif knowsTruth[y]: # y만 알 때
        parent[x] = y
    else:
        parent[x] = y

def countGroups(m, party, parent, knowsTruth):
    cnt = 0
    for i in range(m):
        r = Find(party[i][0], parent) # 대표의 부모 찾기
        if not knowsTruth[r]:
            cnt += 1
    return cnt

def solution(n, m, truth, party):
    parent = [-1] * (n+1)
    knowsTruth = [False] * (n+1)

    for i in truth:
        knowsTruth[i] = True

    for i in range(m):
        fp = party[i][0] # 파티의 대표
        for p in party[i]:
            Union(fp, p, parent, knowsTruth)

    return countGroups(m, party, parent, knowsTruth)

n, m = map(int, input().split())
truth = list(map(int, input().split()))[1:]
party = [list(map(int, input().split()))[1:] for _ in range(m)]

print(solution(n, m, truth, party))
