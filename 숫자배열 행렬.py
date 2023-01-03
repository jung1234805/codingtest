t=int(input())

def nine(num):
    tmp=[]
    for l in range(num):
        num_tmp=''
        for k in range(num - 1, -1, -1):
            num_tmp+=hang[k][l]
        tmp.append(num_tmp)
    return tmp

def eight(num):
    tmp=[]
    for l in range(num-1,-1,-1):
        num_tmp=''
        for k in range(num-1,-1,-1):
            num_tmp += hang[l][k]
        tmp.append(num_tmp)
    return tmp

def two(num):
    tmp=[]
    for l in range(num-1,-1,-1):
        num_tmp=''
        for k in range(num):
            num_tmp += hang[k][l]
        tmp.append(num_tmp)
    return tmp

for i in range(t):
    n=int(input())
    hang=[]
    answer=[0]*n
    for j in range(n):
        hang.append(list(map(str, input().split(' '))))
    first=nine(n)
    second=eight(n)
    third=two(n)
    print('#%d'%(i + 1))
    for p in range(len(first)):
        print(first[p]+' '+second[p]+' '+third[p])

