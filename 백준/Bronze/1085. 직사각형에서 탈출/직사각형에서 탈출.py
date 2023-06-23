x,y,w,h=map(int,input().split())
x_list=[]
x_list.append(x)
x_list.append(y)
if x-w>=0:
    x_list.append(x-w)
else:
    x_list.append(w-x)
if y-h>=0:
    x_list.append(y-h)
else:
    x_list.append(h-y)
print(min(x_list))