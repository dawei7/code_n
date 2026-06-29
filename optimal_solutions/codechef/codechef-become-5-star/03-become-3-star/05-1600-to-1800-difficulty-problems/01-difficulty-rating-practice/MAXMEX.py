import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, mex = (data[idx], data[idx + 1])
        idx += 2
        values = data[idx:idx + n]
        idx += n
        present = set(values)
        if all((value in present for value in range(1, mex))):
            out.append(str(sum((1 for value in values if value != mex))))
        else:
            out.append('-1')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
