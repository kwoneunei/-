N, M = map(int, input().split())
n_list = []
for _ in range(2):
    for _ in range(N):
        n_list.append(list(map(int, input().split())))
for i in range(N):
    for j in range(M):
        n_list[i][j] += n_list[N+i][j]
for i in range(N):
    for j in range(M):
        print(n_list[i][j], end=' ')
    print()