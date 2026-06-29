for _ in range(int(input())):
    n = int(input())
    s = input()
    if s.count('0') == n or s.count('1') == n:
        print(n, 0)
        continue

    dif = s.count('0') - s.count('1')
    print(1, abs(dif) + 1)
    while dif != 0:
        n = len(s)
        for i in range(n):
            if s[i] != s[i+1]:
                which = '0'
                if dif > 0:
                    which = '1'
                s = s[0:i] + which + s[i+2:]
                print(i+1, i+2, which)
                break
        dif = s.count('0') - s.count('1')
    n = len(s)
    print(1, n, 1)
