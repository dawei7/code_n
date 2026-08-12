# Number Rotations - Optimal Approach

## Algorithm Explanation

Find the last $5$ digits of the sum of all integers $N$ ($10 < N < 10^{100}$) such that $N$ divides its right-rotation $R(N)$.

### Algebraic Derivation:
Represent an $L$-digit integer $N$ ($2 \le L \le 100$) ending in digit $d \in [1, 9]$ as:
$$N = 10 A + d$$
where $A$ is the $(L-1)$-digit prefix.

Moving the last digit $d$ to the front yields the right-rotation:
$$R(N) = d \cdot 10^{L-1} + A$$

If $R(N) = k \cdot N$ for some multiplier $k \in [1, 9]$:
$$d \cdot 10^{L-1} + A = k (10 A + d)$$
$$d \cdot 10^{L-1} - k d = (10 k - 1) A$$
$$A = \frac{d (10^{L-1} - k)}{10 k - 1}$$

### Search Procedure:
1. Iterate over lengths $L \in [2, 100]$, last digits $d \in [1, 9]$, and multipliers $k \in [1, 9]$.
2. Compute prefix $A$ if $(10 k - 1) \mid d (10^{L-1} - k)$.
3. Validate that $10^{L-2} \le A < 10^{L-1}$.
4. Accumulate $N = 10 A + d \pmod{10^5}$ into the total sum, formatting the final answer with $5$ leading zero-padded digits.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(L_{\text{max}} \cdot 9 \cdot 9)$ where $L_{\text{max}} = 100$. Runs in $< 0.005\text{s}$.
- **Space Complexity:** $\mathcal{O}(\text{Unique } N)$ - Memory overhead is negligible.
