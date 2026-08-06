def solve(s: str) -> str:
    transformed = "^#" + "#".join(s) + "#$"
    radius = [0] * len(transformed)
    center = right = 0
    best_center = best_length = 0

    for i in range(1, len(transformed) - 1):
        mirror = 2 * center - i
        if i < right:
            radius[i] = min(right - i, radius[mirror])
        while transformed[i + radius[i] + 1] == transformed[i - radius[i] - 1]:
            radius[i] += 1
        if i + radius[i] > right:
            center, right = i, i + radius[i]
        if radius[i] > best_length:
            best_center, best_length = i, radius[i]

    start = (best_center - best_length) // 2
    return s[start : start + best_length]
