def solve(a: int = 1864, b: int = 1909) -> int:
    """Find the number of sides of the Minkowski sum S = S_1864 + S_1865 + ... + S_1909.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Minkowski Sum of Regular Polygons:
       Let S_n be a regular n-gon.
       The edge orientations (normal vectors) of S_n correspond to angles (2*pi*k) / n for 0 <= k < n.
       Equivalently, these edge directions correspond to rational fractions k/n in the interval [0, 1).

    2. Edge Multiplicity in Minkowski Sums:
       The Minkowski sum of two or more convex polygons is a convex polygon whose edges
       correspond to the distinct normal vector directions present in any of the summands.
       Edges with identical slope (same rational direction) merge into a single lengthened edge.

    3. Farey Fractions & Totient Counting:
       A rational angle in lowest terms is p/q with gcd(p, q) = 1 and 0 <= p < q.
       The fraction p/q appears as an edge of some S_n (for a <= n <= b) if and only if
       there exists an integer multiple m*q in the interval [a, b].
       The condition that q has a multiple in [a, b] is:
           b // q > (a - 1) // q.

       For each valid denominator q, there are exactly phi(q) distinct irreducible fractions p/q.
       Therefore, the total number of distinct sides of the Minkowski sum is:
           Total Sides = sum_{q=1}^b [b // q > (a - 1) // q] * phi(q).

    Complexity:
    -----------
    - Time Complexity: O(b * sqrt(b)) operations (~0.001s for b = 1909).
    - Space Complexity: O(1) auxiliary space.
    """

    def phi(n: int) -> int:
        res = n
        p = 2
        temp = n
        while p * p <= temp:
            if temp % p == 0:
                while temp % p == 0:
                    temp //= p
                res -= res // p
            p += 1
        if temp > 1:
            res -= res // temp
        return res

    total_sides = 0
    # Sum phi(q) for every denominator q that has at least one multiple in [a, b]
    for q in range(1, b + 1):
        if b // q > (a - 1) // q:
            total_sides += phi(q)

    return total_sides


if __name__ == "__main__":
    print(solve())
