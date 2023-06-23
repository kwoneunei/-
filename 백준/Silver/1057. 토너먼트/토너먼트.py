N,K,L=map(int,input().split())
x=0
while K!=L:
    K-=(K//2)
    L-=(L//2)
    x+=1
print(x)