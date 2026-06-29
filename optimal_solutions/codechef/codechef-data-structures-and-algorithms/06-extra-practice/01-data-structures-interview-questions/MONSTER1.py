import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    output = []
    for _ in range(t):
        H = int(data[idx])
        X = int(data[idx + 1])
        Y = int(data[idx + 2])
        idx += 3
        if X > Y:
            output.append('1')
        else:
            output.append('0')
    sys.stdout.write('\n'.join(output))


if __name__ == "__main__":
    solve()
