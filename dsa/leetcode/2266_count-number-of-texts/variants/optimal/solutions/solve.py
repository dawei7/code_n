from collections import deque


def solve(pressedKeys: str) -> int:
    modulus = 1_000_000_007

    def count_run(length: int, maximum_press_count: int) -> int:
        recent = deque([1])
        for _ in range(length):
            current = sum(recent) % modulus
            recent.append(current)
            if len(recent) > maximum_press_count:
                recent.popleft()
        return recent[-1]

    answer = 1
    start = 0
    for end in range(1, len(pressedKeys) + 1):
        if end < len(pressedKeys) and pressedKeys[end] == pressedKeys[start]:
            continue
        maximum = 4 if pressedKeys[start] in "79" else 3
        answer = answer * count_run(end - start, maximum) % modulus
        start = end

    return answer
