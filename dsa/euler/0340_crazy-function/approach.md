# Crazy Function - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

For fixed positive integers $a, b, c$, the function $F(n)$ is defined on integers by:
$$F(n) = \begin{cases}
n - c & \text{for } n > b \\
F(a + F(a + F(a + F(a + n)))) & \text{for } n \le b
\end{cases}$$
Let $S(a, b, c) = \sum_{n=0}^b F(n)$.
We are given sample values:
- For $a = 50, b = 2000, c = 40$:
  - $F(0) = 3240$
  - $F(2000) = 2040$
  - $S(50, 2000, 40) = 5\,204\,240$

Find the last $9$ digits of $S(21^7, 7^{21}, 12^7)$ ($S(a, b, c) \bmod 10^9$).

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Recursive Memoization
A direct recursive evaluation with memoization:
- The parameter $b = 7^{21} \approx 5.58 \times 10^{17}$.
- Iterating over $n \in [0, b]$ requires $\approx 5.58 \times 10^{17}$ function evaluations, demanding millions of years of CPU time and petabytes of memoization storage.

---

## 3. Core Intuition & Mathematical Structure

### Unfolding the McCarthy Nested Recurrence
Let $n \in [b - a + 1, b]$:
1. $a + n > b \implies F(a + n) = a + n - c$.
2. $a + F(a + n) = 2a + n - c > b \implies F(a + F(a + n)) = 2a + n - 2c$.
3. $a + F(a + F(a + n)) = 3a + n - 2c > b \implies F(a + F(a + F(a + n))) = 3a + n - 3c$.
4. $a + (3a + n - 3c) = 4a + n - 3c > b \implies F(n) = (4a + n - 3c) - c = n + 4(a - c)$.

For general $n \le b$:
Each block shift of size $a$ downwards ($n \to n - a$) adds an extra $(4a - 3c)$ offset to the outcome:
$$\mathbf{F(n) = n + 4(a - c) + \left\lfloor \frac{b - n}{a} \right\rfloor (4a - 3c)}$$

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Exact Closed-Form Summation
Summing $F(n)$ over $n = 0 \dots b$:
$$S(a, b, c) = \sum_{n=0}^b n + \sum_{n=0}^b 4(a - c) + (4a - 3c) \sum_{n=0}^b \left\lfloor \frac{b - n}{a} \right\rfloor$$
Substituting $u = b - n \in [0, b]$:
1. $\sum_{n=0}^b n = \frac{b(b + 1)}{2}$
2. $\sum_{n=0}^b 4(a - c) = 4(a - c)(b + 1)$
3. Let $q = \lfloor b / a \rfloor$ and $r = b \bmod a$:
   $$\sum_{u=0}^b \left\lfloor \frac{u}{a} \right\rfloor = a \sum_{k=0}^{q-1} k + q(r + 1) = a \frac{q(q - 1)}{2} + q(r + 1)$$
4. Final closed expression:
   $$\mathbf{S(a, b, c) = \frac{b(b + 1)}{2} + 4(a - c)(b + 1) + (4a - 3c) \left( a \frac{q(q - 1)}{2} + q(r + 1) \right)}$$

Evaluating this expression modulo $10^9$ takes $\mathcal{O}(1)$ time.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Verification on $a = 50, b = 2000, c = 40$:
1. $b(b + 1) / 2 = 2000 \times 2001 / 2 = 2\,001\,000$.
2. $4(a - c)(b + 1) = 4(10)(2001) = 80\,040$.
3. $q = 2000 // 50 = 40, \quad r = 2000 \bmod 50 = 0$.
4. $\sum_{u=0}^b \lfloor u / a \rfloor = 50 \times \frac{40 \times 39}{2} + 40(1) = 39\,000 + 40 = 39\,040$.
5. $(4a - 3c) = 200 - 120 = 80 \implies 80 \times 39\,040 = 3\,123\,200$.
6. $S(50, 2000, 40) = 2\,001\,000 + 80\,040 + 3\,123\,200 = \mathbf{5\,204\,240}$. (Matches sample $S(50, 2000, 40) = 5\,204\,240$ exactly! $\checkmark$)

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Exponentiation** | Compute $a = 21^7, b = 7^{21}, c = 12^7$ | $\mathcal{O}(\log \text{exp})$ |
| **Stage 2** | **Quotient & Remainder** | $q = b // a, r = b \bmod a$ | $\mathcal{O}(1)$ |
| **Stage 3** | **Floor Summation** | $\text{sum\_floor} = a \frac{q(q-1)}{2} + q(r + 1)$ | $\mathcal{O}(1)$ |
| **Stage 4** | **Total Sum & Modulo** | Return $(\text{term}_1 + \text{term}_2 + \text{term}_3) \bmod 10^9$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(1)$ | $< 0.001\text{ s}$ execution |
| **Space Complexity** | $\mathcal{O}(1)$ | Scalar variables |
| **Implementation Standard** | $100\%$ Pure Python | Zero external dependencies |

### Critical Invariants & Edge Cases Handled:
1. **Large Number Exponentiation:** Python's arbitrary-precision integers handle $b = 7^{21} \approx 5.58 \times 10^{17}$ with exact precision before modulo reduction.
2. **Remainder $r = 0$ Boundary:** Handled seamlessly by the term $q(r + 1)$.
3. **9-Digit Padding:** Output is formatted as a 9-digit zero-padded string via `f"{ans:09d}"`.
