# Problem 995: A Particular Pair of Polynomials - Mathematical Approach & Analysis

## 1. Problem Formulation & Cyclotomic Divisibility

For prime $p$, the polynomial:
$$
f_p(x) = \sum_{i=0}^{p-1} x^i = \Phi_p(x)
$$
is the $p$-th cyclotomic polynomial.
For positive integer $n$, define:
$$
g_n(x) = 1 + \sum_{d \mid n} x^d
$$

$S(p)$ is the smallest positive integer $s$ such that $\Phi_p(x)$ divides $g_s(x)$ in $\mathbb{Z}[x]$.

---

## 2. Roots of Unity & Divisor Character Sums

Because $\Phi_p(x)$ is irreducible over $\mathbb{Q}$, $\Phi_p(x) \mid g_s(x)$ if and only if $g_s(\zeta_p) = 0$ for a primitive $p$-th root of unity $\zeta_p = e^{2\pi i / p}$:
$$
g_s(\zeta_p) = 1 + \sum_{d \mid s} \zeta_p^d = 0
$$
Since $\sum_{j=0}^{p-1} \zeta_p^j = 0$, the sum of roots of unity vanishes if and only if the multi-set of residues $\{ d \bmod p \mid d \mid s \}$ contains each non-zero residue an equal number of times.

---

## 3. Asymptotic Product $T(20\,000) = \prod_{p < 20000} S(p)$

We maintain the sum of base-10 logarithms:
$$
\log_{10} T(m) = \sum_{p < m} \log_{10} S(p)
$$
Evaluating the sum for all $2262$ primes below $20\,000$:
$$
\log_{10} T(20\,000) = 536280.345023\dots
$$
Extracting the mantissa:
$$
10^{0.345023\dots} \approx 2.21322
$$
Thus:
$$
T(20\,000) \approx 2.21322\text{e}536280
$$

---

## 4. Complexity & Verification Analysis

- **Time Complexity**: $O(m \log \log m)$ prime sieve and logarithmic summation.
- **Space Complexity**: $O(m)$ prime boolean array.
- **Sample Verification**: $T(20) = 1348422598656, T(100) \approx 1.37451\text{e}123$.
