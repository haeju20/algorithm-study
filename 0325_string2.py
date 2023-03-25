a = int(input())
cnt = 0
for _ in range(a):
    w = input()
    f = 0
    for i in range(len(w)-1):
        # 다른 알파벳 등장하면 거기서부터는 new
        if w[i] != w[i+1]:
            new = w[i+1:]
            # new에 이미 등장한 알파벳이 있으면
            if w[i] in new:
                f += 1

    # 연속하지 않는 알파벳이 등장하지 않는다면
    if f == 0:
        cnt += 1
print(cnt)  
