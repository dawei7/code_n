# Pandigital Products - Optimal Approach

## Algorithm Explanation

Find all unique products $P = A \times B$ where the concatenated string of $A$, $B$, and $P$ is a 1-to-9 pandigital arrangement.

### Digit Length Bounds
For $A \times B = P$ to have total length $9$:
1. $1$-digit $\times$ $4$-digit $= 4$-digit product ($1 + 4 + 4 = 9$).
2. $2$-digit $\times$ $3$-digit $= 4$-digit product ($2 + 3 + 4 = 9$).

### Search Strategy:
- Loop $A \in [1, 9]$ and $B \in [1234, \lfloor \frac{9876}{A} \rfloor]$.
- Loop $A \in [12, 98]$ and $B \in [123, \lfloor \frac{9876}{A} \rfloor]$.
- Concatenate string $S = \text{str}(A) + \text{str}(B) + \text{str}(P)$.
- Check if $\text{len}(S) = 9$ and $\text{set}(S) = \{'1', '2', \dots, '9'\}$.
- Collect unique products in a hash set to prevent double counting.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(A \cdot B)$ across bounded search spaces. Runs in $< 0.01\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary set memory.
