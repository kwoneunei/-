n_list = []
m=0
row=0
col=0
for _ in range(9):
    n_list.append(list(map(int, input().split())))
for i in range(9):
    for j in range(9):
        if n_list[i][j]>=m:
            m=n_list[i][j]
            row=i+1
            col=j+1
print(m)
print(row,col)