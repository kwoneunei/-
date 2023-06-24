N=int(input())
n_list=[]
for i in range(N):
    word=sorted(list(input()))
    word=''.join(word)
    if word not in n_list:
        n_list.append(word)
print(len(n_list))