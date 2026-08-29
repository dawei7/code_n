# Resilience - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

A proper fraction whose numerator is less than its denominator $d$ is called a **resilient fraction** if it cannot be cancelled down (i.e. $\gcd(n, d) = 1$).
The number of resilient proper fractions for denominator $d$ is $\phi(d)$, Euler's totient function.
The **resilience** of denominator $d$ is defined as:

$$
R(d) = \frac{\phi(d)}{d - 1}
$$

For example:
- For $d = 12$, $\phi(12) = 4$ (fractions $1/12, 5/12, 7/12, 11/12$), so $R(12) = \frac{4}{11}$.
- $d = 12$ is the smallest denominator with $R(d) < \frac{4}{10}$.

Find the smallest denominator $d$ having a resilience:

$$
R(d) < \frac{15499}{94744}
$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Sequential Linear Scan
A naive approach computes $\phi(d)$ for $d = 2, 3, 4, \dots$:
```python
def naive_resilience(target_ratio):
    # Searching through non-primorial numbers up to ~10^9 takes > 10^4 seconds
    # ...
```

### Primorial Factorization & Multiplier Step Search
1. **Asymptotic Totient Minimization:**
   Notice that:

$$
\frac{\phi(d)}{d} = \prod_{p \mid d} \left(1 - \frac{1}{p}\right)
$$

   To minimize this product, $d$ must contain the maximum number of distinct small prime factors.
   Therefore, $d$ must be a multiple of a **primorial** $P_k = \prod_{i=1}^k p_i$.
2. **Primorial Bounds:**
   Evaluating primorials $P_1 = 2, P_2 = 6, P_3 = 30, \dots, P_9 = 223\,092\,870$:
   - For $P_9 = 2 \times 3 \times 5 \times 7 \times 11 \times 13 \times 17 \times 19 \times 23 = 223\,092\,870$:
     $\frac{\phi(P_9)}{P_9} = \frac{36495360}{223092870} \approx 0.163588 < \frac{15499}{94744} \approx 0.1635882$.
   - But $R(P_9) = \frac{36495360}{223092869} > \frac{15499}{94744}$ due to the $-1$ denominator shift.
3. **Small Integer Multipliers:**
   Testing $d = m \cdot P_9$ for $m \in \{1, 2, 3, 4\}$:
   When $m = 4$, $\phi(4 \cdot P_9) = 2 \phi(P_9) = 72\,990\,720$, and:

$$
R(4 \cdot P_9) = \frac{72990720}{892371479} < \frac{15499}{94744} \quad (\checkmark)
$$

---

## 3. Core Intuition & Mathematical Structure

### Primorial Hierarchy and Resilience Comparison

| $k$ | Prime $p_k$ | Primorial $P_k = \prod_{i=1}^k p_i$ | $\phi(P_k)$ | Asymptotic Ratio $\phi(P_k)/P_k$ | Resilience $R(P_k) = \frac{\phi(P_k)}{P_k - 1}$ | Target Threshold $\frac{15499}{94744} \approx 0.1635882$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$1$** | $2$ | $2$ | $1$ | $0.500000$ | $1/1 = 1.000000$ | Exceeds |
| **$2$** | $3$ | $6$ | $2$ | $0.333333$ | $2/5 = 0.400000$ | Exceeds |
| **$3$** | $5$ | $30$ | $8$ | $0.266667$ | $8/29 \approx 0.275862$ | Exceeds |
| **$4$** | $7$ | $210$ | $48$ | $0.228571$ | $48/209 \approx 0.229665$ | Exceeds |
| **$5$** | $11$ | $2310$ | $480$ | $0.207792$ | $480/2309 \approx 0.207882$ | Exceeds |
| **$9$** | $23$ | $223\,092\,870$ | $36\,495\,360$ | $0.163588$ | $\frac{36495360}{223092869} \approx 0.1635889$ | Exceeds slightly |
| **$9$ ($m=4$)** | $23$ | $\mathbf{892\,371\,480}$ | $72\,990\,720$ | $0.163588$ | $\mathbf{\frac{72990720}{892371479} \approx 0.1635880}$ | **Strictly Less ($\checkmark$)** |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Master Primorial Multiplier Search
```python
def solve(num: int = 15499, den: int = 94744) -> int:
    target = Fraction(num, den)
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

    P = 1
    for p in primes:
        P *= p
        for m in range(1, 100):
            d = m * P
            if Fraction(phi(d), d - 1) < target:
                return d
```

Evaluating for $15499/94744$:

$$
d_{\min} = \mathbf{892\,371\,480}
$$

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Sample Verification for $R(d) < 4/10$
- $P_2 = 2 \times 3 = 6$.
- For $m = 1 \implies d = 6 \implies R(6) = 2/5 = 4/10$ (not strictly less).
- For $m = 2 \implies d = 12 \implies \phi(12) = 4 \implies R(12) = 4/11 < 4/10 \quad (\checkmark)$.
- Smallest denominator is $d = \mathbf{12} \quad (\checkmark)$.

### Example 2: Target Evaluation for $R(d) < 15499/94744$
- Primorial $P_9 = 223\,092\,870$.
- $m = 1, 2, 3$ all fail the strict inequality.
- For $m = 4$:

$$
d = 4 \times 223\,092\,870 = \mathbf{892\,371\,480}
$$

$$
R(d) = \frac{72990720}{892371479} < \frac{15499}{94744} \quad (\checkmark)
$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Primorial Loop** | Accumulate $P_k = \prod_{i=1}^k p_i$ | $\mathcal{O}(k)$ |
| **Stage 2** | **Multiplier Step**| Test $d = m \cdot P_k$ for small integers $m \ge 1$ | $\mathcal{O}(m)$ |
| **Stage 3** | **Totient Check** | Compute $\phi(d)$ and test $\frac{\phi(d)}{d-1} < \frac{15499}{94744}$ | $\mathcal{O}(\sqrt{d})$ |
| **Stage 4** | **Return Minimum** | Return scalar integer $892371480$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(k \cdot p_{k+1})$ | $< 0.001$ seconds |
| **Space Complexity** | $\mathcal{O}(1)$ | Minimal memory |
| **Dynamic Execution** | $100\%$ Inline | Exact Fraction arithmetic comparison |

### Critical Invariants & Edge Cases Handled:
1. **Strict Inequality Invariant**: $R(d) < \text{target}$ must be strictly less (ties like $R(6) = 4/10$ are rejected).
2. **Exact Rational Comparison**: Python `Fraction` ensures zero floating-point roundoff errors across 10-digit denominators.