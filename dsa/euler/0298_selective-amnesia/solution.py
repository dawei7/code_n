"""Project Euler 298: Selective Amnesia

Find the expected value of |L - R| after 50 turns, rounded to 8 decimal places.
Larry uses LRU (Least Recently Used) cache of size 5.
Robin uses FIFO (First In First Out) cache of size 5.
Numbers 1..10 are called uniformly at random each turn.
"""

from __future__ import annotations


def canonicalize(
    larry_mem: list[int] | tuple[int, ...], robin_mem: list[int] | tuple[int, ...]
) -> tuple[tuple[int, ...], tuple[int, ...], int]:
    """Relabels numbers based on first occurrence order in Larry's memory, then Robin's memory."""
    mapping: dict[int, int] = {}
    for x in larry_mem:
        if x not in mapping:
            mapping[x] = len(mapping)
    for x in robin_mem:
        if x not in mapping:
            mapping[x] = len(mapping)
    canon_l = tuple(mapping[x] for x in larry_mem)
    canon_r = tuple(mapping[x] for x in robin_mem)
    return canon_l, canon_r, len(mapping)


def get_transitions(
    state: tuple[tuple[int, ...], tuple[int, ...], int],
) -> list[tuple[tuple[tuple[int, ...], tuple[int, ...], int], float, int]]:
    """Generates all outgoing Markov transitions with probabilities and score difference deltas."""
    larry_mem, robin_mem, num_known = state
    transitions: list[tuple[tuple[tuple[int, ...], tuple[int, ...], int], float, int]] = []

    # 1. Called number is one of the known distinct elements
    for x in range(num_known):
        dl = 1 if x in larry_mem else 0
        dr = 1 if x in robin_mem else 0

        next_l = [x] + [elem for elem in larry_mem if elem != x]
        if len(next_l) > 5:
            next_l = next_l[:5]

        if x in robin_mem:
            next_r = list(robin_mem)
        else:
            next_r = list(robin_mem) + [x]
            if len(next_r) > 5:
                next_r = next_r[1:]

        cl, cr, nk = canonicalize(next_l, next_r)
        transitions.append(((cl, cr, nk), 0.1, dl - dr))

    # 2. Called number is a new, previously uncalled element from the pool of 10
    num_unknown = 10 - num_known
    if num_unknown > 0:
        x = num_known
        next_l = [x] + list(larry_mem)
        if len(next_l) > 5:
            next_l = next_l[:5]

        next_r = list(robin_mem) + [x]
        if len(next_r) > 5:
            next_r = next_r[1:]

        cl, cr, nk = canonicalize(next_l, next_r)
        transitions.append(((cl, cr, nk), num_unknown * 0.1, 0))

    return transitions


def solve(turns: int = 50) -> str:
    """Calculates E[|L - R|] after `turns` rounds using Canonical State Markov Chain Dynamic Programming."""
    start_state = ((), (), 0)
    dp: dict[tuple[tuple[int, ...], tuple[int, ...], int], dict[int, float]] = {
        start_state: {0: 1.0}
    }

    trans_cache: dict[
        tuple[tuple[int, ...], tuple[int, ...], int],
        list[tuple[tuple[tuple[int, ...], tuple[int, ...], int], float, int]],
    ] = {}

    for _ in range(turns):
        next_dp: dict[tuple[tuple[int, ...], tuple[int, ...], int], dict[int, float]] = {}
        for state, dist in dp.items():
            if state not in trans_cache:
                trans_cache[state] = get_transitions(state)
            trans = trans_cache[state]

            for diff, prob in dist.items():
                for next_s, p_trans, delta in trans:
                    nd = diff + delta
                    prob_next = prob * p_trans
                    if next_s not in next_dp:
                        next_dp[next_s] = {}
                    next_dp[next_s][nd] = next_dp[next_s].get(nd, 0.0) + prob_next
        dp = next_dp

    expected_abs_diff = 0.0
    for dist in dp.values():
        for diff, prob in dist.items():
            expected_abs_diff += abs(diff) * prob

    return f"{expected_abs_diff:.8f}"


if __name__ == "__main__":
    print(solve())
