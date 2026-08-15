import math

# Precompute factorials d! for digits d = 0..9
FACTS = [math.factorial(d) for d in range(10)]


def next_term(n: int) -> int:
    """Compute the sum of factorials of digits of n."""
    return sum(FACTS[int(c)] for c in str(n))


def solve(limit: int = 1000000, target_length: int = 60) -> int:
    """Find how many digit factorial chains starting below limit (1,000,000) contain exactly 60 non-repeating terms.

    Mathematical Principles Applied:
    1. Digit Factorial Sequence Map:
       Let f(n) = sum_{c in str(n)} c!.
       Sequence S(n_0) = (n_0, n_1, n_2, ...) where n_{k+1} = f(n_k).
       Because the digit factorial function maps any integer to a bounded range (6 * 9! = 2,540,160),
       every sequence eventually enters a cycle.

    2. Memoized Path Length DP & Cycle Detection:
       Track visited path to detect new cycles and memoize chain lengths in a hash map `memo[x]`.
       - For terms in a cycle of length L: memo[term] = L.
       - For terms along a tail leading into a known chain: memo[tail_i] = base_len + i.

    Time Complexity: O(limit) memoized execution in ~0.70s.
    Space Complexity: O(limit) memory for memo dictionary.
    """
    memo = {}

    def get_chain_length(n: int) -> int:
        """Evaluate non-repeating chain length starting at n using memoized cycle tracking."""
        path = []
        curr = n

        # Trace sequence until entering memoized node or hitting a cycle within current path
        while curr not in memo and curr not in path:
            path.append(curr)
            curr = next_term(curr)

        # Case 1: Entry into previously computed memoized path
        if curr in memo:
            base_len = memo[curr]
        # Case 2: New cycle detected within current path
        else:
            idx = path.index(curr)
            loop_len = len(path) - idx
            # Assign loop length to all nodes inside the cycle
            for i in range(idx, len(path)):
                memo[path[i]] = loop_len
            base_len = loop_len
            path = path[:idx]

        # Memoize tail nodes leading to cycle or known path
        for i, val in enumerate(reversed(path), 1):
            memo[val] = base_len + i

        return memo[n]

    # Count starting numbers 1 <= i < 1,000,000 obtaining exactly target_length (60) non-repeating terms
    exact_60_count = sum(1 for i in range(1, limit) if get_chain_length(i) == target_length)

    # Return total count of 60-term digit factorial chains
    return exact_60_count


if __name__ == "__main__":
    print(solve())
