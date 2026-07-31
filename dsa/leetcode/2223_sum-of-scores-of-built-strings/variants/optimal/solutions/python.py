def solve(s: str) -> int:
    length = len(s)
    z = [0] * length
    left = 0
    right = 0
    for index in range(1, length):
        if index <= right:
            z[index] = min(right - index + 1, z[index - left])
        while (
            index + z[index] < length
            and s[z[index]] == s[index + z[index]]
        ):
            z[index] += 1
        if index + z[index] - 1 > right:
            left = index
            right = index + z[index] - 1
    return length + sum(z)
