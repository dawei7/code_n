def solve(nums: list[int]) -> int:
    n = len(nums)
    score = sum(value <= index for index, value in enumerate(nums))
    changes = [0] * n

    for index, value in enumerate(nums):
        changes[(index - value + 1) % n] -= 1
        changes[(index + 1) % n] += 1

    best_rotation = 0
    best_score = score
    for rotation in range(1, n):
        score += changes[rotation]
        if score > best_score:
            best_score = score
            best_rotation = rotation
    return best_rotation
