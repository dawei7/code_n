# Sub-string Divisibility - Optimal Approach

## Algorithm Explanation

Find the sum of all $0$-to-$9$ pandigital numbers $d_1 d_2 \dots d_{10}$ whose consecutive $3$-digit substrings $d_{i+1} d_{i+2} d_{i+3}$ are divisible by the $i$-th prime $P \in [2, 3, 5, 7, 11, 13, 17]$.

1. Iterate all permutations of digits `"0123456789"` ($10! = 3,628,800$ arrangements).
2. Skip arrangements starting with `'0'`.
3. Test substring divisibility condition for each prime in $[2, 3, 5, 7, 11, 13, 17]$ with early exit.
4. Sum all matching $10$-digit integers.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(10! \cdot 7)$ where $10! = 3.6 \times 10^6$. With early termination, runs in $< 0.45\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Memory is constant.
