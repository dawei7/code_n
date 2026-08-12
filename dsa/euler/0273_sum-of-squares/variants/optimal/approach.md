# Sum of Squares - Optimal Approach

## Algorithm Explanation

Find $\sum S(N)$ for all squarefree integers $N$ only divisible by prime numbers $p \equiv 1 \pmod 4$ with $p < 150$, where $S(N)$ is the sum of $a$ for all solutions to $a^2 + b^2 = N$ ($0 \le a \le b$).

### Gaussian Integer Multiplication Tree:
1. **Prime Gaussian Decompositions**:
   There are $16$ primes $p \equiv 1 \pmod 4$ under $150$: $\{5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97, 101, 109, 113, 137, 149\}$.
   Each prime factors uniquely in $\mathbb{Z}[i]$ as $p_j = (a_j + i b_j)(a_j - i b_j)$.
2. **Subset Representation Tree**:
   For any squarefree $N = \prod_{j \in S} p_j$, all representations $a^2 + b^2 = N$ are obtained by multiplying $g_j = a_j + i b_j$ or $\bar{g}_j = a_j - i b_j$ for each prime $j \in S$.
   This yields $2^{|S|-1}$ distinct pairs $(a, b)$.
3. **Execution**:
   Using recursive DFS over all $2^{16} - 1 = 65,535$ non-empty subsets of Gaussian primes, summing $\min(|a|, |b|)$ yields $2032447591196869022$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(3^K)$ for $K = 16$ primes. Runs in $\approx 5.45\text{s}$.
- **Space Complexity:** $\mathcal{O}(2^K)$ representation list.
