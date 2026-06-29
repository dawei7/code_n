def rep(s):
    ones = 0
    gap = 0
    cnt = False
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '1':
            cnt = not cnt
            ones += 1
        elif cnt:
            gap += 1
    if ones == 0:
        return 0, len(s)
    else:
        return ones, gap, len(s)


def solve(s):
    classes = set()
    for i in range(len(s)):
        z = [0, 0]
        ones = 0
        cur_par = 0
        for j in range(i, len(s)):
            if s[j] == '1':
                ones += 1
                cur_par = 1 - cur_par
            else:
                z[cur_par] += 1
            L = j - i + 1
            if ones == 0:
                r = 0, L
            else:
                r = ones, z[1 - cur_par], L
            classes.add(r)
    return classes


for i in range(int(input())):
    n = input()
    print(len(solve(n)))


if __name__ == "__main__":
    solve()
