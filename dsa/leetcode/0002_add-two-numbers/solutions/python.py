def solve(l1: list[int], l2: list[int]) -> list[int]:
    result: list[int] = []
    carry = 0
    i = 0
    while i < len(l1) or i < len(l2) or carry:
        left = l1[i] if i < len(l1) else 0
        right = l2[i] if i < len(l2) else 0
        carry, digit = divmod(left + right + carry, 10)
        result.append(digit)
        i += 1
    return result
