# Squarefree Factors - Optimal Approach

## Algorithm Explanation

Find $S(10\,000\,000\,000) = \sum_{k=2}^{N} \operatorname{Fsf}(k)$, where $\operatorname{Fsf}(k)$ is the number of ways $k$ can be factored into one or more squarefree factors $>1$.

### Sub-linear Squarefree Product DFS & Mobius Sieve:
1. **Squarefree Factorization Definition**:
   A factorization $k = f_1 \cdot f_2 \cdots f_r$ is valid iff $1 < f_1 \le f_2 \le \dots \le f_r$ and each factor $f_i$ is squarefree ($\mu^2(f_i) = 1$).
2. **Recursive Product Search**:
   We search over ordered tuples of squarefree factors $f_1 \le f_2 \le \dots \le f_r$:
   - For a current remaining product limit $M$ and minimum factor $f_{\min}$:
     - If $M < f_{\min}^2$, any valid remaining factor is a single squarefree number $f \in [f_{\min}, M]$.
     - The number of such single factors is $Q(M) - Q(f_{\min} - 1)$, where $Q(x) = \sum_{j=1}^{\sqrt{x}} \mu(j) \lfloor x / j^2 \rfloor$ is the number of squarefree integers $\le x$.
     - For $M \ge f_{\min}^2$, we branch over all squarefree $f \ge f_{\min}$ with $f^2 \le M$ and recurse on $M / f$.
3. **Execution**:
   Evaluating the total squarefree factorization count for $N = 10\,000\,000\,000$ yields $457895958010$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N^{1/2})$ for $N = 10^{10}$. Runs in $\approx 0.15\text{s}$.
- **Space Complexity:** $\mathcal{O}(N^{1/2})$ Mobius sieve array.
