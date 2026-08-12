# Modular Cubes, Part 2 - Optimal Approach

## Algorithm Explanation

Find the sum of all positive integers $n \le 10^{11}$ for which $C(n) = 242$, where $C(n)$ is the number of solutions to $x^3 \equiv 1 \pmod n$ for $1 < x < n$.

### Prime Factorization Characterization & Recursive Backtracking:
1. **Total Cube Root Count**:
   $C(n) = 242 \iff C(n) + 1 = 243 = 3^5$ total solutions to $x^3 \equiv 1 \pmod n$.
2. **Prime Contribution Rules**:
   A prime power $p^k \mid\mid n$ contributes a factor of $3$ to the total root count if:
   - $p \equiv 1 \pmod 3$ for any $k \ge 1$.
   - $p = 3$ for $k \ge 2$.
   All other prime powers contribute $1$.
3. **5-Factor Search Classes**:
   $n \le 10^{11}$ must contain exactly $5$ factors of $3$, corresponding to:
   - Class 1: $5$ distinct primes $p_1, p_2, p_3, p_4, p_5 \equiv 1 \pmod 3$.
   - Class 2: $4$ distinct primes $p_1, p_2, p_3, p_4 \equiv 1 \pmod 3$ and $9 \mid n$.
4. **Execution**:
   Using recursive DFS over combinations of primes $\equiv 1 \pmod 3$ combined with sum-of-multiples sieves for remaining factors, the sum of all valid $n \le 10^{11}$ is $8495585919506151122$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(L^{3/4})$ for $L = 10^{11}$. Runs in $\approx 2.10\text{s}$.
- **Space Complexity:** $\mathcal{O}(\sqrt{L})$ prime array.
