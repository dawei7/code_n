# Special Subset Sums: Optimum - Optimal Approach

## Algorithm Explanation

Find the optimum special sum set $A$ of size $n = 7$ that minimizes $S(A)$ and return its concatenated set string.

### Special Sum Set Verification:
A set $A = \{a_1 < a_2 < \dots < a_n\}$ is a special sum set if:
1. **Disjoint Subset Sum Uniqueness**: $S(B) \ne S(C)$ for any non-empty disjoint subsets $B, C$.
2. **Cardinality Monotonicity**: $|B| > |C| \implies S(B) > S(C)$.
   - Sufficient condition: $\sum_{i=1}^{k+1} a_i > \sum_{i=0}^{k-1} a_{n-i}$ for $1 \le k < \lceil n/2 \rceil$.

### Near-Optimum Anchor Search:
From $n = 6$ optimum set $\{11, 18, 19, 20, 22, 25\}$, applying the recursive shift rule with middle element $b = 20$ yields anchor $A_7' = \{20, 31, 38, 39, 40, 42, 45\}$.
Bounding local delta search $a_i' \in [a_i - 3, a_i + 3]$ checks candidate 7-tuples and finds the global minimum sum set string.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(7^7 \cdot 2^7)$ ($823543 \times 128 \approx 10^8$ operations). Runs in $< 0.8\text{s}$.
- **Space Complexity:** $\mathcal{O}(2^7)$ - Subset sum hash set.
