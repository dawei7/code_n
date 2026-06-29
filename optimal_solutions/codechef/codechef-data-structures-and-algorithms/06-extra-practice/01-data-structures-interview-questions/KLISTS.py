import sys

def solve():
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    res = []
    for _ in range(t):
        k = int(data[index])
        x = int(data[index + 1])
        index += 2
        count = 0
        for _ in range(k):
            n = int(data[index])
            index += 1
            lst = list(map(int, data[index:index + n]))
            index += n
            mn = min(lst)
            mx = max(lst)
            if mn // x == mx // x:
                count += 1
        res.append(str(count))
    sys.stdout.write('\n'.join(res))


if __name__ == "__main__":
    solve()
