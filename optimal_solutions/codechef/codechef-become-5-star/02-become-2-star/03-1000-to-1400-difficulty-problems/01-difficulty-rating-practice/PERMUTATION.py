import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        values = sorted(data[idx:idx + n])
        idx += n
        next_target = 1
        operations = 0
        possible = True
        for value in values:
            target = max(next_target, value)
            if target > n:
                possible = False
                break
            operations += target - value
            next_target = target + 1
        out.append(str(operations if possible else -1))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
