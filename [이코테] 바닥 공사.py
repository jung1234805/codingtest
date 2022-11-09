'''
가로의 길이가 N, 세로의 길이가 2인 직사각형 형태의 얇은 바닥이 있다. 태일이는 이 얇은 바닥을 1X2의 덮개, 2X1의 덮개, 2X2의 덮개를 이용해 채우고자 한다.
이때 바닥을 채우는 모든 경우의 수를 구하는 프로그램을 작성하시오. 예를 들어 2X3 크기의 바닥을 채우는 경우의 수는 5가지이다.
'''

n=int(input())

d=[0]*1001

d[1]=1
d[2]=3

for i in range(3,n+1):
    d[i]=d(d[i-1]+2 * d[i-2])%796796

print(d[n])
