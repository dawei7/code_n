## Description

You are given an integer array `nums` and a positive integer `k`. For any array, its frequency score is formed by considering each distinct value $x$, raising $x$ to the number of times it occurs, summing those terms, and reducing the sum modulo $10^9 + 7$. For example, `[5, 4, 5, 7, 4, 4]` has score $(5^2 + 4^3 + 7^1) \bmod (10^9 + 7) = 96$.

Consider every contiguous subarray of `nums` whose length is exactly `k`. Return the largest of their frequency scores. The comparison is between the values after applying the modulus; the unreduced mathematical sums are not what must be maximized.
