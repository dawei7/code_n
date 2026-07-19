from collections import deque


def solve(forbidden: list[int], a: int, b: int, x: int) -> int:
    blocked = set(forbidden)
    limit = max(max(forbidden), x) + a + b
    queue = deque([(0, False, 0)])
    visited = {(0, False)}

    while queue:
        position, last_was_backward, jumps = queue.popleft()
        if position == x:
            return jumps

        forward = position + a
        forward_state = (forward, False)
        if forward <= limit and forward not in blocked and forward_state not in visited:
            visited.add(forward_state)
            queue.append((forward, False, jumps + 1))

        backward = position - b
        backward_state = (backward, True)
        if (
            not last_was_backward
            and backward >= 0
            and backward not in blocked
            and backward_state not in visited
        ):
            visited.add(backward_state)
            queue.append((backward, True, jumps + 1))

    return -1
