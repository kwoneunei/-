N=int(input())
x=N
for i in range(1,N):
    print("*"*i," "*((2*x)-4),"*"*i)
    x-=1
print("*"*2*N)
for i in range(N-1):
    print("*"*(N-1)," "*(i*2),"*"*(N-1))
    i+=2
    N-=1