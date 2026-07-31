def solve(s: str, k: int) -> str:
    while len(s) > k:
        groups = []
        for start in range(0, len(s), k):
            group_sum = sum(int(digit) for digit in s[start : start + k])
            groups.append(str(group_sum))
        s = "".join(groups)
    return s
