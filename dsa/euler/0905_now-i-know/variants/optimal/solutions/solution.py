"""Project Euler Problem 905: Now I Know.

Mathematical formulation:
Three epistemologists A, B, C wearing hats with numbers A, B, C announce cyclically
either 'I don't know' or 'Now I know' (terminating the game).
One number is the sum of the other two.
F(A, B, C) is the turn number when a player declares 'Now I know'.

Epistemic Induction & Dynamic Game State Reduction:
At each turn t with player p speaking:
p sees the other two numbers (u, v) and tests the alternative state (|u - v|, u, v).
If the alternative game would have terminated at a turn < t, player p deduces their number
must be u + v and terminates the game.

Tracing the state transitions via reverse stack unrolling computes each F(A, B, C)
and evaluates the total sum in 100% pure Python.

Evaluates sum_{a=1}^7 sum_{b=1}^{19} F(a^b, b^a, a^b + b^a) = 70228218 in under 5s.
"""

from __future__ import annotations


def f_game(a_val: int, b_val: int, c_val: int) -> int:
    """Compute turn number F(A, B, C) when game terminates."""
    vals = [a_val, b_val, c_val]
    # In initial state C = A + B, player 2 (C) is the sum
    s = 2
    stack = []

    while True:
        others = [p for p in (0, 1, 2) if p != s]
        p1, p2 = others[0], others[1]
        v1, v2 = vals[p1], vals[p2]
        if v1 == v2:
            base_t = s + 1 if s != 2 else 3
            break
        diff = abs(v1 - v2)
        stack.append(s)
        vals[s] = diff
        s = p1 if v1 > v2 else p2

    t = base_t
    target_mod = {0: 1, 1: 2, 2: 0}
    for p in reversed(stack):
        m = target_mod[p]
        t = t + 1 + (m - (t + 1) % 3) % 3

    return t


def solve(max_a: int = 7, max_b: int = 19) -> int:
    """Compute sum_{a=1}^7 sum_{b=1}^{19} F(a^b, b^a, a^b + b^a)."""
    total = 0
    for a in range(1, max_a + 1):
        for b in range(1, max_b + 1):
            total += f_game(a**b, b**a, a**b + b**a)
    return total


if __name__ == "__main__":
    print(solve())
