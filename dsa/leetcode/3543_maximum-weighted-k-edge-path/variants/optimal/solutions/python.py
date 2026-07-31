def solve(
    n: int,
    edges: list[list[int]],
    k: int,
    t: int,
) -> int:
    states = [1] * n
    limit = (1 << t) - 1

    for _ in range(k):
        next_states = [0] * n
        for source, target, weight in edges:
            next_states[target] |= (
                states[source] << weight
            ) & limit
        states = next_states

    return max(states).bit_length() - 1
