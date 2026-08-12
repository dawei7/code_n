# Special Partitions - Optimal Approach

## Algorithm Explanation

Find the sum of all prime numbers $q < 1\,000\,000$ such that $P(q) = 1$, where $P(n)$ is the number of valid partitions of $n$ into terms of the form $2^i 3^j$ ($i, j \ge 0$) such that no term divides any other term.

### Monotonic Exponent Anti-chain DFS:
1. **Divisibility Anti-chain Condition**:
   A term $2^a 3^b$ divides $2^c 3^d$ iff $a \le c$ and $b \le d$.
   To ensure no term divides another in a valid partition, as $i$ increases, exponent $j$ must strictly decrease.
2. **Recursive Partition Enumeration**:
   We precompute all terms $2^i 3^j < 1\,000\,000$ grouped by exponent $i$.
   Using memoized depth-first search (DFS) with strictly decreasing $j$ constraints, we compute $P(n)$ for all $n < 1\,000\,000$.
3. **Execution**:
   Filtering all prime integers $q < 1\,000\,000$ with $P(q) = 1$ and summing them yields $3053105$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \cdot T)$ for $N = 1\,000\,000$ and term count $T \approx 100$. Runs in $\approx 1.80\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ frequency table.
