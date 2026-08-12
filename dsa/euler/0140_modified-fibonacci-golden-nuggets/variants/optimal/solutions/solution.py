def solve(target_count: int = 30) -> int:
    """Find sum of the first 30 Modified Fibonacci Golden Nuggets.
    
    Time Complexity: O(target_count)
    Space Complexity: O(1)
    """
    seeds = [
        (7, 1), (8, 2), (13, 5), (17, 7), (32, 14), (43, 19),
        (-7, 1), (-8, 2), (-13, 5), (-17, 7), (-32, 14), (-43, 19)
    ]

    n_set = set()

    for k0, y0 in seeds:
        k, y = k0, y0
        for _ in range(target_count + 5):
            if (k - 7) % 5 == 0:
                n = (k - 7) // 5
                if n > 0:
                    n_set.add(n)
            k_next = 9 * k + 20 * y
            y_next = 4 * k + 9 * y
            k, y = k_next, y_next

    sorted_n = sorted(n_set)
    return sum(sorted_n[:target_count])
