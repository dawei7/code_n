import itertools


def solve(target_triangles: int = 47547) -> int:
    """Find smallest integer that can be length of cathetus of exactly target_triangles right triangles.
    
    Time Complexity: O(Factors_Permutations)
    Space Complexity: O(1)
    """
    target = 2 * target_triangles + 1  # 95095
    factors = [19, 13, 11, 7, 5]
    primes = [3, 5, 7, 11, 13, 17, 19]

    min_a = float('inf')

    for f_even in factors:
        e = (f_even + 1) // 2
        rem_factors = [f for f in factors]
        rem_factors.remove(f_even)

        for perm in itertools.permutations(rem_factors):
            a = 2**e
            for i, f_odd in enumerate(perm):
                e_i = (f_odd - 1) // 2
                a *= primes[i]**e_i
            if a < min_a:
                min_a = a

    return int(min_a)
