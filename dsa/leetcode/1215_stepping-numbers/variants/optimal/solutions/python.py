from collections import deque


def solve(low: int, high: int) -> list[int]:
    result = [0] if low == 0 else []
    queue = deque(range(1, 10))

    while queue:
        number = queue.popleft()
        if number > high:
            continue
        if number >= low:
            result.append(number)

        last_digit = number % 10
        if last_digit > 0:
            child = number * 10 + last_digit - 1
            if child <= high:
                queue.append(child)
        if last_digit < 9:
            child = number * 10 + last_digit + 1
            if child <= high:
                queue.append(child)

    return result
