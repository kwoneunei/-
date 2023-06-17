N=int(input())
N_list=list(map(int,input().split()))
y=len(N_list)
i=0
rc=0
while i<len(N_list): 
    if N_list[i]!=i+1:
        N_list.pop(i)
        rc+=1
    else:
        i+=1
print(rc)