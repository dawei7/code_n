def solve(s, t, k):
    if len(s) != len(t):
        return False

    used = [0] * 26
    for source, target in zip(s, t):
        shift = (ord(target) - ord(source)) % 26
        if shift == 0:
            continue
        move = shift + 26 * used[shift]
        if move > k:
            return False
        used[shift] += 1

    return True
