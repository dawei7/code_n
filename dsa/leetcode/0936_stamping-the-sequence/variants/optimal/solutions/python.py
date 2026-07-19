"""Optimal app-local solution for LeetCode 936."""

from collections import deque


def solve(stamp, target):
    stamp_length = len(stamp)
    target_length = len(target)
    window_count = target_length - stamp_length + 1
    made_positions = []
    unresolved = []
    dependents = [[] for _ in range(target_length)]

    for start in range(window_count):
        made = []
        todo = set()
        for offset, stamp_character in enumerate(stamp):
            position = start + offset
            if target[position] == stamp_character:
                made.append(position)
            else:
                todo.add(position)
                dependents[position].append(start)
        made_positions.append(made)
        unresolved.append(todo)

    erased = [False] * target_length
    used_window = [False] * window_count
    queue = deque()
    reverse_moves = []

    def use_window(start):
        used_window[start] = True
        reverse_moves.append(start)
        for position in made_positions[start]:
            if not erased[position]:
                erased[position] = True
                queue.append(position)

    for start in range(window_count):
        if not unresolved[start]:
            use_window(start)

    while queue:
        position = queue.popleft()
        for start in dependents[position]:
            unresolved[start].discard(position)
            if not unresolved[start] and not used_window[start]:
                use_window(start)

    if not all(erased):
        return []
    return reverse_moves[::-1]
