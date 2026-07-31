from itertools import permutations


def _merge(first: str, second: str) -> str:
    if second in first:
        return first

    for overlap in range(min(len(first), len(second)), 0, -1):
        if first.endswith(second[:overlap]):
            return first + second[overlap:]
    return first + second


def solve(a: str, b: str, c: str) -> str:
    best: str | None = None
    for order in permutations((a, b, c)):
        candidate = _merge(_merge(order[0], order[1]), order[2])
        if best is None or (len(candidate), candidate) < (len(best), best):
            best = candidate

    assert best is not None
    return best
