import math


FACTS = [math.factorial(d) for d in range(10)]


def next_term(n: int) -> int:
    return sum(FACTS[int(c)] for c in str(n))


def solve(limit: int = 1000000, target_length: int = 60) -> int:
    """Find how many chains starting with a number below limit contain exactly target_length non-repeating terms.
    
    Time Complexity: O(limit)
    Space Complexity: O(limit)
    """
    memo = {}

    def get_chain_length(n: int) -> int:
        path = []
        curr = n
        while curr not in memo and curr not in path:
            path.append(curr)
            curr = next_term(curr)

        if curr in memo:
            base_len = memo[curr]
        else:
            idx = path.index(curr)
            loop_len = len(path) - idx
            for i in range(idx, len(path)):
                memo[path[i]] = loop_len
            base_len = loop_len
            path = path[:idx]

        for i, val in enumerate(reversed(path), 1):
            memo[val] = base_len + i

        return memo[n]

    return sum(1 for i in range(1, limit) if get_chain_length(i) == target_length)
