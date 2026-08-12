# Square Remainders - Optimal Approach

## Algorithm Explanation

Find $\sum_{a=3}^{1000} r_{\max}(a)$ where $r$ is the remainder when $(a-1)^n + (a+1)^n$ is divided by $a^2$.

### Binomial Expansion Modulo $a^2$:
Expanding terms modulo $a^2$:
$$(a-1)^n = (-1)^n + n(-1)^{n-1} a + \mathcal{O}(a^2)$$
$$(a+1)^n = 1 + n a + \mathcal{O}(a^2)$$

Summing both terms:
- For $n$ **even**: $(a-1)^n + (a+1)^n \equiv 2 \pmod{a^2}$.
- For $n$ **odd**: $(a-1)^n + (a+1)^n \equiv 2na \pmod{a^2}$.

### Remainder Maximization:
To maximize $2na \pmod{a^2}$ with $2na < a^2$:
- If $a$ is **even**: $r_{\max}(a) = a(a - 2)$.
- If $a$ is **odd**: $r_{\max}(a) = a(a - 1)$.

Sum $r_{\max}(a)$ across all $a \in [3, 1000]$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(A)$ where $A = 1000$. Runs in $< 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary memory is constant.
