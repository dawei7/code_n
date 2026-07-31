from collections import deque


def solve(nums: list[int], start: int, goal: int) -> int:
    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        value, operations = queue.popleft()
        for operand in nums:
            for candidate in (
                value + operand,
                value - operand,
                value ^ operand,
            ):
                if candidate == goal:
                    return operations + 1
                if 0 <= candidate <= 1000 and candidate not in visited:
                    visited.add(candidate)
                    queue.append((candidate, operations + 1))

    return -1
