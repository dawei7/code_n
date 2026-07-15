"""Optimal app-local solution for LeetCode 913."""

from collections import deque


def solve(graph):
    DRAW, MOUSE, CAT = 0, 1, 2
    MOUSE_TURN, CAT_TURN = 0, 1
    n = len(graph)

    outcome = [[[DRAW, DRAW] for _ in range(n)] for _ in range(n)]
    degree = [[[0, 0] for _ in range(n)] for _ in range(n)]

    for mouse in range(n):
        for cat in range(1, n):
            degree[mouse][cat][MOUSE_TURN] = len(graph[mouse])
            degree[mouse][cat][CAT_TURN] = sum(
                neighbor != 0 for neighbor in graph[cat]
            )

    queue = deque()
    for cat in range(1, n):
        for turn in (MOUSE_TURN, CAT_TURN):
            outcome[0][cat][turn] = MOUSE
            queue.append((0, cat, turn, MOUSE))

    for node in range(1, n):
        for turn in (MOUSE_TURN, CAT_TURN):
            outcome[node][node][turn] = CAT
            queue.append((node, node, turn, CAT))

    while queue:
        mouse, cat, turn, winner = queue.popleft()

        if turn == MOUSE_TURN:
            parents = (
                (mouse, previous_cat, CAT_TURN)
                for previous_cat in graph[cat]
                if previous_cat != 0
            )
        else:
            parents = (
                (previous_mouse, cat, MOUSE_TURN)
                for previous_mouse in graph[mouse]
            )

        for parent_mouse, parent_cat, parent_turn in parents:
            if outcome[parent_mouse][parent_cat][parent_turn] != DRAW:
                continue

            player = MOUSE if parent_turn == MOUSE_TURN else CAT
            if winner == player:
                outcome[parent_mouse][parent_cat][parent_turn] = winner
                queue.append((parent_mouse, parent_cat, parent_turn, winner))
                continue

            degree[parent_mouse][parent_cat][parent_turn] -= 1
            if degree[parent_mouse][parent_cat][parent_turn] == 0:
                outcome[parent_mouse][parent_cat][parent_turn] = winner
                queue.append((parent_mouse, parent_cat, parent_turn, winner))

    return outcome[1][2][MOUSE_TURN]

