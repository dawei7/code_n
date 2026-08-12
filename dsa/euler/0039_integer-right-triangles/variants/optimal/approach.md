# Integer Right Triangles - Optimal Approach

## Algorithm Explanation

Find the perimeter $p \le 1000$ that maximizes the number of integer right triangle solutions $\{a, b, c\}$.

### Parity Deduction
Since $a^2 + b^2 = c^2$, the perimeter $p = a + b + c$ must always be **even**.

### Algebraic Solution
From $c = p - a - b$ and $a^2 + b^2 = c^2$:
$$b = \frac{p^2 - 2pa}{2p - 2a}$$

1. Iterate even perimeters $p \in [2, 4, \dots, 1000]$.
2. Iterate side $a \in [1, \lfloor \frac{p}{3} \rfloor]$.
3. If $(p^2 - 2pa) \bmod (2p - 2a) = 0$, increment solution count for $p$.
4. Return perimeter $p$ with the highest count.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(P^2)$ where $P = 1000$. Runs in $< 0.01\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary memory is constant.
