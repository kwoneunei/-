N,M=map(int,input().split())
x=0
if N>=M:
    x+=N-1
    x+=N*(M-1)
else:
    x+=M-1
    x+=M*(N-1)
print(x)