n = int(input())

result = 0
# Please write your code here.
def reg(count):
    global result

    if count == 0:
        result += 1
        return

    for i in range(1, 5):
        if count - i >= 0:
            reg(count - i)

reg(n)
print(result)