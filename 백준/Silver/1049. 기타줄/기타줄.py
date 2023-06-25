N,M=map(int,input().split())
n_list=[]
A_list=[]
B_list=[]
min_list=[]
for i in range(M):
    n_list.extend(map(int,input().split()))
for _ in range(M):
    A_list.append(n_list[_*2])
    B_list.append(n_list[(_*2)+1])
if N<=6:
    for i in range(M):
        min_list.append(A_list[i])
        min_list.append(B_list[i]*N)
else:
  for i in range((N//6)+1):
    min_list.append(min(A_list)*(i)+min(B_list)*(N-(6*i)))
  min_list.append(min(A_list)*((N//6)+1))
print(min(min_list))