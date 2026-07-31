def solve(n: int) -> int:
    bits = f"{n:b}"
    flips = 0
    left = 0
    right = len(bits) - 1

    while left < right:
        if bits[left] != bits[right]:
            flips += 2
        left += 1
        right -= 1

    return flips
