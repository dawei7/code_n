from collections import defaultdict


def solve(lights: list[list[int]]) -> int:
    changes: dict[int, int] = defaultdict(int)
    for position, radius in lights:
        changes[position - radius] += 1
        changes[position + radius + 1] -= 1

    brightness = 0
    maximum = 0
    answer = 0
    for position in sorted(changes):
        brightness += changes[position]
        if brightness > maximum:
            maximum = brightness
            answer = position

    return answer
