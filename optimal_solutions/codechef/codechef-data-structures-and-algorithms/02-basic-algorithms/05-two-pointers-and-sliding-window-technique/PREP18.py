def min_diff(a, b, c):
    i = j = k = 0
    best = float('inf')
    while i < len(a) and j < len(b) and (k < len(c)):
        curr_min = min(a[i], b[j], c[k])
        curr_max = max(a[i], b[j], c[k])
        best = min(best, curr_max - curr_min)
        if curr_min == a[i]:
            i += 1
        elif curr_min == b[j]:
            j += 1
        else:
            k += 1
    return best

def solve():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        na = int(data[index])
        nb = int(data[index + 1])
        nc = int(data[index + 2])
        index += 3
        A = list(map(int, data[index:index + na]))
        index += na
        B = list(map(int, data[index:index + nb]))
        index += nb
        C = list(map(int, data[index:index + nc]))
        index += nc
        results.append(min_diff(A, B, C))
    sys.stdout.write('\n'.join(map(str, results)))


if __name__ == "__main__":
    solve()
