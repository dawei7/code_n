def solve(a: str, b: str) -> str:
    left = len(a) - 1
    right = len(b) - 1
    carry = 0
    result: list[str] = []

    while left >= 0 or right >= 0 or carry:
        total = carry
        if left >= 0:
            total += ord(a[left]) - ord("0")
            left -= 1
        if right >= 0:
            total += ord(b[right]) - ord("0")
            right -= 1
        result.append(str(total & 1))
        carry = total >> 1

    return "".join(reversed(result))
