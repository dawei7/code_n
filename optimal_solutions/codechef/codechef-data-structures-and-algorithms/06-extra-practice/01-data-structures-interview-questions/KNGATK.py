import sys

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    index = 1
    res = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        temps = list(map(int, data[index:index + n]))
        index += n
        temps.sort()
        res.append(str(temps[1]))
    sys.stdout.write('\n'.join(res))


if __name__ == "__main__":
    solve()
