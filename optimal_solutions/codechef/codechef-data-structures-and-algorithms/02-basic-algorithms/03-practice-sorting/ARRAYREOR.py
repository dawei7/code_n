import sys

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    index = 1
    res = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        A = list(map(int, data[index:index + n]))
        index += n
        B = list(map(int, data[index:index + n]))
        index += n
        A.sort(reverse=True)
        B.sort()
        res.append(' '.join(map(str, A)) + ' ')
        res.append(' '.join(map(str, B)) + ' ')
    sys.stdout.write('\n'.join(res))


if __name__ == "__main__":
    solve()
