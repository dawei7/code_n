from collections import Counter


def solve(nums: list[int]) -> list[int]:
    numbers = sorted(nums)
    target_length = len(numbers) // 2

    for candidate in numbers[1:]:
        difference = candidate - numbers[0]
        if difference <= 0 or difference % 2:
            continue

        remaining = Counter(numbers)
        recovered: list[int] = []
        for lower in numbers:
            if remaining[lower] == 0:
                continue
            higher = lower + difference
            if remaining[higher] == 0:
                break
            remaining[lower] -= 1
            remaining[higher] -= 1
            recovered.append(lower + difference // 2)

        if len(recovered) == target_length:
            return recovered

    return []
