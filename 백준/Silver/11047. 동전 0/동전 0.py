A,B=map(int,input().split())
N_list=[]
x=0
for i in range(A):
    N_list.append(int(input()))
for i in range(1,A+1):
    x+=B//N_list[-i]
    B=B%N_list[-i]
print(x)