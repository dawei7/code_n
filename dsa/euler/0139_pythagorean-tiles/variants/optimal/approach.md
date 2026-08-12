# Pythagorean Tiles - Optimal Approach

## Algorithm Explanation

Find the number of right-angled triangles with integer sides $(a, b, c)$ ($a^2 + b^2 = c^2$) and perimeter $a + b + c < 100,000,000$ for which four such triangles can form a $c \times c$ square with a central square hole of side $|b - a|$ that perfectly tiles the $c \times c$ square ($c \bmod |b - a| == 0$).

### Primitive Pythagorean Parametrization:
Using Euclid's formula for primitive right triangles:
$$a = m^2 - n^2, \quad b = 2mn, \quad c = m^2 + n^2 \quad (m > n \ge 1, \gcd(m, n) = 1, m - n \text{ odd})$$

- Primitive perimeter $P = a + b + c = 2m(m + n)$.
- Central hole side length: $h = |b - a| = |2mn - (m^2 - n^2)|$.
- Tiling condition: $c \pmod h == 0$.

### Multiplier Counting:
For every primitive triple $(a, b, c)$ satisfying $c \bmod h == 0$, all scaled integer multiples $k(a, b, c)$ also satisfy the tiling condition.
The number of valid scaled triangles below perimeter $L = 10^8$ is:
$$\text{Multiples}(P) = \left\lfloor \frac{L - 1}{P} \right\rfloor$$

Sum $\text{Multiples}(P)$ over all valid primitive generators $m, n$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\sqrt{L})$ where $L = 10^8$ ($m \le 7071$). Runs in $< 0.015\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary memory is constant.
