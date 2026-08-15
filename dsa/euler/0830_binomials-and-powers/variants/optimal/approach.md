# Binomials and Powers - Optimal Approach

## 1. Problem Statement & Mathematical Formulation

Define $S(n) = \sum_{k=0}^{n} \binom{n}{k} k^n$. We seek $S(10^{18}) \pmod{M}$ where $M = 83^3 \times 89^3 \times 97^3$.

---

## 2. Naive Approach & Computational Impossibility

### Direct Summation
Evaluating $S(10^{18})$ directly requires iterating $k = 0$ to $10^{18}$, computing $\binom{10^{18}}{k}$ and $k^{10^{18}}$ for each term. This is $> 10^{18}$ iterations, each involving modular exponentiation — completely infeasible.

---

## 3. Mathematical Breakthrough & Applied Theorems

### Mahler $p$-adic Truncation & Chinese Remainder Theorem
1. **Forward Difference Reformulation**: Using the identity $S(n) = \sum_{j=0}^{n} \binom{n}{j} \Delta^j(x^n)\big|_{x=0} \cdot 2^{n-j}$, where $\Delta^j(x^n)\big|_{x=0} = \sum_{i=0}^{j} (-1)^{j-i} \binom{j}{i} i^n$ is the $j$-th forward difference of $x^n$ evaluated at $x = 0$.

2. **Mahler's $p$-adic Convergence**: For the function $f(x) = x^n$ on $\mathbb{Z}_p$, Mahler's theorem guarantees $v_p(\Delta^j f(0)) \ge \lfloor j/(p-1) \rfloor$. Therefore $\Delta^j(x^n) \equiv 0 \pmod{p^3}$ for all $j \ge 3(p-1)+1$. Since the largest prime is $97$, all terms with $j \ge 289$ vanish modulo every $p^3$ in the modulus. Padding to $j = 300$ provides safety.

3. **Euler Totient Exponent Reduction**: For $\gcd(i, p) = 1$, $i^n \equiv i^{n \bmod \phi(p^3)} \pmod{p^3}$ where $\phi(p^3) = p^2(p-1)$. For $p \mid i$ and $n \ge 3$, $i^n \equiv 0 \pmod{p^3}$.

4. **CRT Recombination**: Compute the sum modulo each of $83^3$, $89^3$, $97^3$ independently, then reconstruct modulo $M$ via CRT.

---

## 4. Step-by-Step Mathematical Algorithm

1. Set $n = 10^{18}$, primes $= [83, 89, 97]$, and $M = \prod p_i^3$.
2. Precompute $\binom{n}{j}$ for $j = 0, \dots, 300$ using the recurrence $\binom{n}{j} = \binom{n}{j-1} \cdot (n-j+1)/j$ (exact integer division).
3. For each prime $p$ with modulus $m = p^3$ and $\phi = p^2(p-1)$:
   - For $j = 0, \dots, 300$: compute $a_j = \sum_{i=0}^{j} (-1)^{j-i} \binom{j}{i} i^{n \bmod \phi} \pmod{m}$, skipping multiples of $p$ (contributing 0).
   - Accumulate $R_p = \sum_{j=0}^{300} \binom{n}{j} \cdot a_j \cdot 2^{n-j} \pmod{m}$.
4. Combine $R_{83}$, $R_{89}$, $R_{97}$ via CRT to obtain $S(10^{18}) \bmod M$.

---

## 5. Implementation Architecture & Mechanics

The solution is implemented in `solution.py`:
- **`solve(n)`**: $\mathcal{O}(\sum_p \text{limit}^2)$ Mahler truncation solver with CRT assembly.
- Binomial coefficients are computed as exact Python integers, then reduced modulo each $p^3$ inside the inner loop.
- Modular exponentiation uses Python's built-in `pow(base, exp, mod)` with three arguments.

---

## 6. Mathematical Complexity Analysis

- **Time Complexity**: $\mathcal{O}(\sum_p \text{limit}^2)$ where limit $= 300$. The inner double loop is $\sum_{j=0}^{300} j \approx 45\,000$ modular exponentiations per prime, totalling $\sim 135\,000$ `pow` calls. Constant with respect to $n$.
- **Space Complexity**: $\mathcal{O}(\text{limit})$ for the 301-element binomial and difference coefficient arrays.
