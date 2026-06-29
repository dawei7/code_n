def solve():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    result = []
    pos = 1
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        s = data[pos]
        pos += 1
        max_len = 1
        for i in range(n):
            l, r = (i, i)
            while l >= 0 and r < n and (s[l] == s[r]):
                curr_len = r - l + 1
                if curr_len > max_len:
                    max_len = curr_len
                l -= 1
                r += 1
            l, r = (i, i + 1)
            while l >= 0 and r < n and (s[l] == s[r]):
                curr_len = r - l + 1
                if curr_len > max_len:
                    max_len = curr_len
                l -= 1
                r += 1
        result.append(str(max_len))
    sys.stdout.write('\n'.join(result))


if __name__ == "__main__":
    solve()
