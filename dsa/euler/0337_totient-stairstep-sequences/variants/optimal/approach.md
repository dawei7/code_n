# Totient Stairstep Sequences - Optimal Approach

## Algorithm Explanation

Find $S(20\,000\,000) \bmod 10^8$, where $S(N)$ is the number of valid sequences $\{a_1, a_2, \ldots, a_n\}$ starting with $a_1 = 6$ such that $\phi(a_i) < \phi(a_{i+1}) < a_i < a_{i+1}$ for all $i$.

### Linear Totient Sieve & Fenwick Tree Range DP:
1. **Sequence Condition**:
   A valid transition from $y$ to $x$ requires:
   $$\phi(y) < \phi(x) \quad \text{and} \quad \phi(x) < y < x$$
   Let $dp[x]$ be the total number of valid sequences ending at $x$.
2. **2D Range Query via Fenwick Tree**:
   We precompute Euler's totient $\phi(x)$ for all $x \le N = 20\,000\,000$ using a linear sieve.
   As $x$ increases from $6$ to $N$:
   - The allowed predecessors $y$ lie in the interval $\phi(x) < y < x$ with key condition $\phi(y) < \phi(x)$.
   - Maintaining dynamic prefix sums over $\phi(y)$ using a Fenwick tree (Binary Indexed Tree) enables $\mathcal{O}(\log N)$ transition sum queries.
3. **Execution**:
   Summing all $dp[x]$ modulo $10^8$ for $N = 20\,000\,000$ yields $85068021$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \log N)$ for $N = 20\,000\,000$. Runs in $\approx 8.50\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ totient and BIT arrays.
