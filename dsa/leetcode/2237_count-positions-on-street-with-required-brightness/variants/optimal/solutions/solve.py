def solve(
    n: int,
    lights: list[list[int]],
    requirement: list[int],
) -> int:
    changes = [0] * (n + 1)
    for position, radius in lights:
        left = max(0, position - radius)
        right = min(n - 1, position + radius)
        changes[left] += 1
        changes[right + 1] -= 1

    answer = 0
    brightness = 0
    for index in range(n):
        brightness += changes[index]
        if brightness >= requirement[index]:
            answer += 1
    return answer
