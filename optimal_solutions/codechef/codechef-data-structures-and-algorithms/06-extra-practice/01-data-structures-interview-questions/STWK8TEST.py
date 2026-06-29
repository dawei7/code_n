def solve():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    groups = []
    for _ in range(n):
        group = list(map(int, data[idx:idx + m]))
        idx += m
        groups.append(group)
    group_max = [max(group) for group in groups]
    col_min = [101] * m
    for i in range(n):
        for j in range(m):
            if groups[i][j] < col_min[j]:
                col_min[j] = groups[i][j]
    found = False
    for i in range(n):
        for j in range(m):
            if groups[i][j] == group_max[i] and groups[i][j] == col_min[j]:
                found = True
                break
        if found:
            break
    sys.stdout.write('Yes' if found else 'No')


if __name__ == "__main__":
    solve()
