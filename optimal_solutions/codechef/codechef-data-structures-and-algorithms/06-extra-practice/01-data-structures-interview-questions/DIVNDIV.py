def solve():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    output = []
    idx = 1
    for _ in range(t):
        X = int(data[idx])
        Y = int(data[idx + 1])
        Z = int(data[idx + 2])
        idx += 3
        if Y % Z == 0:
            output.append('-1')
            continue
        candidate = (X // Y + 1) * Y
        if candidate % Z != 0:
            output.append(str(candidate))
        else:
            output.append(str(candidate + Y))
    sys.stdout.write('\n'.join(output))


if __name__ == "__main__":
    solve()
