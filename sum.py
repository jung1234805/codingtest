answer=[]


for t in range(10):
    i=int(input())
    max_col=0
    plat=[]
    for j in range(100):
        m = list(map(int, input().split()))
        sum_m=sum(m)
        if sum_m>max_col:
            max_col=sum_m
        plat.append(m)

    for k in range(100):
        sum_k=0
        for l in range(100):
            tmp=plat[l][k]
            sum_k=sum_k+tmp
        if sum_k>max_col:
            max_col=sum_k
    right=0
    for p in range(100):
        right=right+plat[p][p]
    if right>max_col:
        max_col=right
    left_sum=0
    for o in range(100):
        left=plat[o][-(o+1)]
        left_sum=left_sum+left
    if left_sum>max_col:
        max_col=left_sum
    answer.append(max_col)

for u in range(len(answer)):
    print("#%d %d"%(u+1,answer[u]))