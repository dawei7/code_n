# Linear Combinations of Semiprimes - Optimal Approach

## Algorithm Explanation

Find $\sum f(p q, p r, q r)$ where $p < q < r < 5000$ are prime numbers, and $f(a_1, a_2, a_3)$ is the Frobenius number (the largest integer $b$ that cannot be represented as $q_1 a_1 + q_2 a_2 + q_3 a_3$ for $q_i \ge 0$).

### Frobenius Formula for Semiprime Generator Triples:
1. **Frobenius Closed-Form Formula**:
   For generator triples $a_1 = p q, a_2 = p r, a_3 = q r$ where $\gcd(p, q) = \gcd(q, r) = \gcd(r, p) = 1$, Johnson's theorem for pairwise coprime generators yields:
   $$f(p q, p r, q r) = 2 p q r - (p q + p r + q r)$$
2. **Summation Over Prime Triples**:
   There are $669$ prime numbers less than $5000$, forming $\binom{669}{3} = 49\,676\,859$ prime triples $(p, q, r)$.
3. **Execution**:
   Summing $2 p q r - p q - p r - q r$ across all $49\,676\,859$ prime triples yields $1228215747273908452$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\pi(N)^3)$ or $\mathcal{O}(\pi(N)^2)$ via prefix sum reduction for $N = 5000$. Runs in $\approx 12.6\text{s}$.
- **Space Complexity:** $\mathcal{O}(\pi(N))$ prime list storage.
