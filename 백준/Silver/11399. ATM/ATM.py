A=int(input())
B_list=list(map(int,input().split()))
B_list.sort()
y=len(B_list)
x=0
for i in range(len(B_list)):
    x+=B_list[i]*y
    y-=1
print(x)