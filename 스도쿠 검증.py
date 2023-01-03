t=int(input())
tmp=[0]*t
x=[0,1,2,0,1,2,0,1,2]
y=[0,0,0,1,1,1,2,2,2]

def check(dx,dy):
    d_tmp=0
    for p in range(len(x)):
        d_tmp+=sdq[dy+y[p]][dx+x[p]]
    if d_tmp==45:
        return True
    else:
        return False

for i in range(t):
    answer=1
    sdq=[]
    for j in range(9):
        input_list=list(map(int, input().split(' ')))
        if sum(input_list)!=45:
            sdq.append(input_list)
            answer=0
        else:
            sdq.append(input_list)
    a=check(0,0)
    b=check(0,3)
    c=check(0,6)
    d=check(3,0)
    e=check(3,3)
    f=check(3,6)
    g=check(6,0)
    h=check(6,3)
    t=check(6,6)
    if a==False or b==False or c==False or d==False or e==False or f==False or g==False or h==False or t==False:
        answer=0
    for l in range(9):
        sum_tmp=0
        for m in range(9):
            sum_tmp+=sdq[m][l]
        if sum_tmp!=45:
            answer = 0
            break
    tmp[i]=answer

for c in range(len(tmp)):
    print('#%d %d'%(c+1,tmp[c]))


