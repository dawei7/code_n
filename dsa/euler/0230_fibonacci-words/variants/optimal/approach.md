# Fibonacci Words - Optimal Approach

## Algorithm Explanation

Find $\sum_{n=0}^{17} 10^n \times D_{A,B}((127 + 19n) \times 7^n)$ for 100-digit string prefixes $A$ and $B$ from $\pi$.

### Recursive Binary Decompositions & Fibonacci Sequence Search:
1. **Length Sequence**:
   For concatenated terms $W_k = W_{k-2} W_{k-1}$ with $|A| = |B| = 100$, lengths follow $L_k = L_{k-2} + L_{k-1}$ ($L_1 = 100, L_2 = 100$).
2. **Path Decomposition**:
   To locate digit $n$ in $W_k$:
   - If $n \le L_{k-2}$, the digit lies in $W_{k-2}$ at index $n$.
   - If $n > L_{k-2}$, the digit lies in $W_{k-1}$ at index $n - L_{k-2}$.
   This reduces target $n$ to base string $A$ or $B$ in $\mathcal{O}(\log_\phi n)$ logarithmic steps.
3. **Execution**:
   Evaluating the digit search across $n \in [0, 17]$ yields $850481152593119296$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(M \cdot \log_\phi N)$ where $M = 18$ queries and $N \approx 10^{17}$. Runs in $\approx 0.000\text{s}$.
- **Space Complexity:** $\mathcal{O}(\log_\phi N)$ for Fibonacci length table.
