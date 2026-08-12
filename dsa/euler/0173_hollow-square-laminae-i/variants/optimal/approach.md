# Hollow Square Laminae I - Optimal Approach

## Algorithm Explanation

Find the number of different square laminae that can be formed using up to $N = 1,000,000$ tiles.

### Factor Pair Transformation:
A square lamina with outer side $a$ and inner square hole side $b$ uses $n = a^2 - b^2$ tiles where $a > b \ge 1$ and $a \equiv b \pmod 2$.

Factoring $a^2 - b^2$:
$$n = (a - b)(a + b) \le N$$

Let $u = a - b$ and $v = a + b$. Since $a$ and $b$ have the same parity, $u$ and $v$ are both even positive integers ($v \ge u + 2$).
Let $u = 2x$ and $v = 2y$ ($1 \le x < y$):
$$n = 4 x y \le N \implies x y \le \frac{N}{4} = M$$

Finding the number of valid laminae is equivalent to counting integer pairs $(x, y)$ such that:
$$1 \le x < y \quad \text{and} \quad x y \le M$$

For a fixed $x \in [1, \lfloor \sqrt{M} \rfloor]$, $y$ can take any integer value in $[x + 1, \lfloor M / x \rfloor]$.
$$\text{Total Laminae} = \sum_{x=1}^{\lfloor \sqrt{M} \rfloor} \left( \lfloor \frac{M}{x} \rfloor - x \right)$$

For $N = 1,000,000$ ($M = 250,000$): $\sqrt{M} = 500$ iterations.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\sqrt{N})$ where $N = 10^6$ ($500$ iterations). Runs in $< 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Constant space.
