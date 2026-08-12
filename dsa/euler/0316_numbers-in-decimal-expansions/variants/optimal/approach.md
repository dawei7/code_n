# Numbers in Decimal Expansions - Optimal Approach

## Algorithm Explanation

Find $\sum_{n=2}^{999999} g\left(\left\lfloor\frac{10^{16}}{n}\right\rfloor\right)$, where $g(k)$ is the expected first 1-based starting position of the digit string $k$ in an infinite sequence of random uniform decimal digits.

### Guibas-Odlyzko String Martingale Formula:
1. **Martingale Expected Index Formula**:
   By Conway's Gambling / Guibas-Odlyzko theorem, the expected first occurrence index $g(S)$ of a string $S$ of length $L = |S|$ in a random $10$-ary sequence is:
   $$g(S) = \sum_{j=1}^{L} 10^j \cdot [S[1..j] = S[L-j+1..L]] - (L - 1)$$
   where $[S[1..j] = S[L-j+1..L]]$ checks if the prefix of length $j$ is equal to the suffix of length $j$ (a border of $S$).
2. **Fast Evaluation**:
   For each integer $N = \lfloor 10^{16} / n \rfloor$ ($n \in [2, 999999]$), we extract its decimal string $S$, identify all border lengths $j \in [1, L]$, and evaluate $g(N)$ in $\mathcal{O}(L)$ time.
3. **Execution**:
   Summing $g(\lfloor 10^{16} / n \rfloor)$ for all $2 \le n \le 999999$ yields $542934735751917735$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(M \cdot L)$ for $M = 1\,000\,000$ and string length $L \le 16$. Runs in $\approx 1.29\text{s}$.
- **Space Complexity:** $\mathcal{O}(L)$ string allocation.
