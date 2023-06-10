N=int(input())
x=1
for i in range(1,N+1):
    print(" "*(N-1),"*"*x,sep='')
    x+=2
    N-=1