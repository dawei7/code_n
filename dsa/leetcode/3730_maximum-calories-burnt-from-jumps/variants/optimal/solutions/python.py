def solve(heights: list[int]) -> int:
    ordered = sorted(heights)
    left = 0
    right = len(ordered) - 1
    previous = 0
    result = 0

    while left <= right:
        current = ordered[right]
        right -= 1
        result += (previous - current) ** 2
        previous = current

        if left <= right:
            current = ordered[left]
            left += 1
            result += (previous - current) ** 2
            previous = current

    return result
