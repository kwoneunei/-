N=int(input())
x=0
A=list(map(int,input().split()))
B=list(map(int,input().split()))
for i in range(N):
    x+=max(A)*min(B)
    A.remove(max(A))
    B.remove(min(B))
print(x)