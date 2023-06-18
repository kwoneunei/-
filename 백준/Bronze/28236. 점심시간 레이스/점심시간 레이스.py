n,m,k=map(int,input().split())
N_list=[]
for i in range(k):
    A,B=map(int,input().split())
    N_list.append(A+m-B)
print(N_list.index(min(N_list))+1)