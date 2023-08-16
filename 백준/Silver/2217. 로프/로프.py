A=int(input())
B=[]
for i in range(A):
    B.append(int(input()))
B.sort()
C=[]
D=A
for i in range(A):
    C.append(B[i]*D)
    D-=1
print(max(C))