def rearrange_string(s):
    n = len(s)
    t = [''] * n
    l = 0
    r = n - 1
    start = False
    for i in range(n - 1, -1, -1):
        if start:
            t[l] = s[i]
            l += 1
        else:
            t[r] = s[i]
            r -= 1
        if s[i] in 'aeiou':
            start = not start
    return ''.join(t)

def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    t = int(data[0])
    results = []
    index = 1
    for _ in range(t):
        n = int(data[index])
        s = data[index + 1]
        result = rearrange_string(s)
        results.append(result)
        index += 2
    print('\n'.join(results))


if __name__ == "__main__":
    solve()
