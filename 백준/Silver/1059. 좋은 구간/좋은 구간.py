L=int(input())
L_list=[]
L_list.extend(map(int,input().split()))
L_list.append(0)
x_list=[]
a_list=[]
b_list=[]
y=0
n=int(input())
for _ in range(L+1):
    x_list.append(L_list[_]-n)
for _ in range(L+1):
    if x_list[_]<0:
        a_list.append(x_list[_])
    elif x_list[_]>0:
        b_list.append(x_list[_])
    else:
        a_list.append(x_list[_])
        b_list.append(x_list[_])
if max(a_list)==0 and min(b_list)==0:
    y=0
else:
    A=max(a_list)+n+1
    B=min(b_list)+n-1
    for i in range(A,B+1):
        for j in range(i+1,B+1):
            if n>=i and n<=j:
                y+=1
print(y)