# Nim - Optimal Approach

## Algorithm Explanation

Find the number of positive integers $n \le 2^{30}$ such that the Nim sum $X(n, 2n, 3n) = n \oplus 2n \oplus 3n = 0$.

### Bitwise Addition & Fibonacci Counting:
1. **Nim Sum Equivalence**:
   Since $3n = n + 2n$, $n \oplus 2n \oplus (n + 2n) = 0 \iff n \oplus 2n = n + 2n$.
2. **No Consecutive Ones Condition**:
   Bitwise XOR equals arithmetic sum iff there are no carry bits during addition:
   $$n \oplus 2n = n + 2n \iff n \text{ AND } 2n = 0$$
   This condition holds iff the binary representation of $n$ contains no consecutive `1`s.
3. **Fibonacci Closed-Form Count**:
   The number of binary integers of length $\le k$ without consecutive `1`s is given by the Fibonacci number $F_{k+2}$.
4. **Execution**:
   For $k = 30$, evaluating $F_{32}$ yields $2178309$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(K)$ for $K = 30$. Runs in $\approx 0.00\text{s}$.
- **Space Complexity:** $\mathcal{O}(K)$.
