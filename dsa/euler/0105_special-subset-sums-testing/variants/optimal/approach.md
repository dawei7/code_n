# Special Subset Sums: Testing - Optimal Approach

## Algorithm Explanation

Identify all special sum sets among $100$ candidate sets in `sets.txt` ($7 \le n \le 12$) and return the total sum of $S(A)$ for all valid sets.

### Validation Rules:
For a sorted set $A = \{a_1 < a_2 < \dots < a_n\}$:
1. **Rule 2 (Cardinality Monotonicity)**:
   - Check $\sum_{i=1}^{k+1} a_i > \sum_{i=0}^{k-1} a_{n-i}$ for $1 \le k < \lceil n/2 \rceil$.
   - Fails fast in $\mathcal{O}(n)$ steps if false.
2. **Rule 1 (Subset Sum Uniqueness)**:
   - Generate all $2^n - 1$ non-empty subset sums using `itertools.combinations`.
   - Reject set if any sum collision occurs.

Accumulate $S(A) = \sum_{a \in A} a$ for all valid sets.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(100 \cdot 2^N)$ where $N \le 12$ ($100 \times 4096 \approx 4 \times 10^5$ operations). Runs in $< 0.12\text{s}$.
- **Space Complexity:** $\mathcal{O}(2^N)$ - Hash set subset sum cache.
