from itertools import product, groupby

K, N = map(int, input().split())

# Please write your code here.
ls = product(range(1, K+1), repeat=N)

for data in ls:
    if all(len(list(g)) < 3 for _, g in groupby(data)):
        print(*data)
