# Criss Cross - Optimal Approach

## Algorithm Explanation

Find the total number of ways to fill a $4 \times 4$ grid with digits $0 \le d \le 9$ such that all $4$ rows, $4$ columns, and $2$ main diagonals sum to the same integer value $S \in [0, 36]$.

### Linear Algebra & Variable Reduction:
Label grid cells:
$$\begin{matrix}
a & b & c & d \\
e & f & g & h \\
i & j & k & l \\
m & n & o & p
\end{matrix}$$

Solving the system of $10$ linear equations yields exact linear substitutions for $8$ variables in terms of free variables $(a, b, c, d, e, f, g, i)$:
1. $S = a + b + c + d$
2. $h = S - e - f - g$
3. $m = S - a - e - i$
4. $j = a + e + i - d - g$
5. $p = e + i - d$
6. $l = f + g - i$
7. $n = S - b - f - j$
8. $k = S - a - f - p$
9. $o = S - c - g - k$

### Precomputed Sum Groups & Bounded Iteration:
Precompute 4-digit tuples grouped by sum $S$.
Bounded search range for $i$: $i \in [\max(0, f+g-9), \min(9, f+g)]$.
Verify digit bounds $0 \le d_i \le 9$ for all cells and check final diagonal equations.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\sum_S |\text{Tuples}(S)|^2 \cdot \text{Range}(i))$. Runs in $\approx 15\text{s}$.
- **Space Complexity:** $\mathcal{O}(10^4)$ - Tuple lookup dictionary.
