def solve(target_n: int = 30) -> int:
    """Find a_30 where a_n is the n-th digit power sum number >= 10.
    
    Time Complexity: O(B * E)
    Space Complexity: O(B * E)
    """
    results = set()

    for base in range(2, 100):
        for e in range(2, 50):
            val = base**e
            if val >= 10:
                if sum(int(c) for c in str(val)) == base:
                    results.add(val)

    sorted_results = sorted(results)
    return sorted_results[target_n - 1]
