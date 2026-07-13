def solve(arr, m, k):
    if m <= 0 or k <= 0:
        return False
    total = m * k
    for start in range(0, len(arr) - total + 1):
        ok = True
        for offset in range(m, total):
            if arr[start + offset] != arr[start + offset - m]:
                ok = False
                break
        if ok:
            return True
    return False
