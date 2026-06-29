for _ in range(int(input())):
    n = int(input())
    s = input()
    if len(s) != n: print(-1)
    zero, one = 0, 0
    for i in range(n):
        if s[i] == '0':
            if i%2 == 0: zero += 1
            else: zero -= 1
        else:
            if i%2 == 0: one += 1
            else: one -= 1
    if zero == 0 or one == 0: print('Yes')
    else: print('No')
