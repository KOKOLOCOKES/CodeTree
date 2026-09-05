from itertools import product

K, N = map(int, input().split())

# Please write your code here.
ls = [i for i in range(1, K+1)]
temp = product(ls, repeat=N)

for seq in temp:
    print(*seq)
