def solve(pairs: list[list[int]]) -> int:
    chain_length = 0
    chain_end = float("-inf")

    for left, right in sorted(pairs, key=lambda pair: pair[1]):
        if left > chain_end:
            chain_length += 1
            chain_end = right
    return chain_length
