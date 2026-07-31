from itertools import permutations


def solve(a: str, b: str, c: str) -> str:
    def merge(first: str, second: str) -> str:
        if second in first:
            return first

        for overlap in range(min(len(first), len(second)), 0, -1):
            if first.endswith(second[:overlap]):
                return first + second[overlap:]
        return first + second

    best = None
    for order in permutations((a, b, c)):
        candidate = merge(merge(order[0], order[1]), order[2])
        if best is None or (len(candidate), candidate) < (len(best), best):
            best = candidate

    return best
