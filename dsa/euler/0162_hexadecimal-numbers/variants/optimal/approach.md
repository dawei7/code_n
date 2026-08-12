# Hexadecimal Numbers - Optimal Approach

## Algorithm Explanation

Find the total number of hexadecimal numbers with at most $16$ digits (no leading zeroes) that contain the digits $0$, $1$, and $\text{A}$ at least once, formatted as an uppercase hexadecimal string.

### Inclusion-Exclusion Principle by Length $L$:
For a hexadecimal string of length $L$ ($3 \le L \le 16$):
The first digit cannot be $0$ ($15$ choices: $1 \dots \text{F}$).

Define conditions:
- $A_0$: Does not contain $0$.
- $A_1$: Does not contain $1$.
- $A_{\text{A}}$: Does not contain $\text{A}$.

Evaluating set sizes by first digit and remaining $L-1$ digit choices:
- $|S| = 15 \times 16^{L-1}$
- $|A_0| = 15 \times 15^{L-1}$
- $|A_1| = 14 \times 15^{L-1}$
- $|A_{\text{A}}| = 14 \times 15^{L-1}$
- $|A_0 \cap A_1| = 14 \times 14^{L-1}$
- $|A_0 \cap A_{\text{A}}| = 14 \times 14^{L-1}$
- $|A_1 \cap A_{\text{A}}| = 13 \times 14^{L-1}$
- $|A_0 \cap A_1 \cap A_{\text{A}}| = 13 \times 13^{L-1}$

By Principle of Inclusion-Exclusion:
$$\text{Valid}(L) = 15 \cdot 16^{L-1} - 43 \cdot 15^{L-1} + 41 \cdot 14^{L-1} - 13 \cdot 13^{L-1}$$

Sum $\text{Valid}(L)$ for $L \in [3, 16]$ and format result as uppercase hexadecimal string.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(L)$ where $L = 16$. Runs in $< 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Memory overhead is constant.
