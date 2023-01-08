t=int(input())
tmp=[]
for i in range(t):
    n,m=map(int, input().split(' '))
    if n>m:
        longer=list(map(int,input().split(' ')))
        shor=list(map(int,input().split(' ')))
    else:
        shor = list(map(int, input().split(' ')))
        longer = list(map(int, input().split(' ')))
    round=len(longer)-len(shor)+1
    x_max = 0
    for j in range(round):
        div=longer[j:j+len(shor)]
        x_find=0
        for l in range(len(shor)):
            x_find=x_find+(shor[l]*div[l])
        x_max=max(x_max,x_find)

    tmp.append(x_max)


for k in range(len(tmp)):
    print('#%d %d'%(k+1,tmp[k]))