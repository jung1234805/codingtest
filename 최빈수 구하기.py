t=int(input())
answer=[]
for i in range(t):
    n=int(input())
    tmp=[0]*101
    grade=list(map(int,input().split()))

    for j in grade:
        tmp[j]+=1
    m=max(tmp)
    ind=list(filter(lambda x: tmp[x] == m, range(len(tmp))))
    answer.append(max(ind))

for l in range(len(answer)):
    print('#%d %d'%(l+1, answer[l]))
