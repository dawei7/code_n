# Powerful Digit Counts - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

The 5-digit number $16\,807 = 7^5$ is also a fifth power. Similarly, the 9-digit number $134\,217\,728 = 8^9$ is a ninth power.

Let $L(x) = \lfloor \log_{10} x \rfloor + 1$ denote the number of decimal digits of positive integer $x$.

The objective is to find how many $n$-digit positive integers exist which are also an $n$-th power:
$$N_{\text{powers}} = \left| \left\{ (a, n) \in \mathbb{N}^2 \;\middle|\; L(a^n) = n \right\} \right|$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Unbounded Search Loop
A naive algorithm tests unrestricted pairs $(a, n)$:
```python
def naive_powerful_digit_counts():
    # loops over a and n without analytical bounds
    # ...
```

### Analytical Bounds on Base and Exponent
1. **Base Constraint $a \le 9$:** If $a \ge 10$, then $a^n \ge 10^n$, which contains at least $n + 1$ digits for all $n \ge 1$. Therefore, the base MUST satisfy $1 \le a \le 9$.
2. **Exponent Constraint $n \le \lfloor \frac{1}{1 - \log_{10} a} \rfloor$:**
   $$10^{n-1} \le a^n < 10^n \implies n - 1 \le n \log_{10} a \implies n(1 - \log_{10} a) \le 1 \implies n \le \frac{1}{1 - \log_{10} a}$$
   For $a = 9$:
   $$n \le \frac{1}{1 - \log_{10} 9} \approx \frac{1}{1 - 0.95424} = \frac{1}{0.04576} \approx 21.85 \implies n \le 21$$

---

## 3. Core Intuition & Mathematical Structure

### Exponent Limits for Bases $a \in [1, 9]$

| Base $a$ | Logarithm $\log_{10} a$ | Bound Formula $\frac{1}{1 - \log_{10} a}$ | Maximum Exponent $n_{\text{max}}$ | Valid Powers Count |
| :---: | :---: | :---: | :---: | :---: |
| **$1$** | $0.0000$ | $1.000$ | $1$ ($1^1 = 1$) | $1$ |
| **$2$** | $0.3010$ | $1.430$ | $1$ ($2^1 = 2$) | $1$ |
| **$3$** | $0.4771$ | $1.912$ | $1$ ($3^1 = 3$) | $1$ |
| **$4$** | $0.6021$ | $2.513$ | $2$ ($4^1=4, 4^2=16$) | $2$ |
| **$5$** | $0.6990$ | $3.322$ | $3$ ($5^1 \dots 5^3=125$) | $3$ |
| **$6$** | $0.7782$ | $4.508$ | $4$ ($6^1 \dots 6^4=1296$) | $4$ |
| **$7$** | $0.8451$ | $6.455$ | $6$ ($7^1 \dots 7^5=16807 \dots$) | $6$ |
| **$8$** | $0.9031$ | $10.319$ | $10$ ($8^1 \dots 8^9=134217728 \dots$) | $10$ |
| **$9$** | $0.9542$ | $21.854$ | $21$ ($9^1 \dots 9^{21}$) | $21$ |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Closed-Form Analytical Sum
Summing the maximum exponents across all 9 possible bases:
$$N_{\text{powers}} = \sum_{a=1}^9 \left\lfloor \frac{1}{1 - \log_{10} a} \right\rfloor$$
$$N_{\text{powers}} = 1 + 1 + 1 + 2 + 3 + 4 + 6 + 10 + 21 = \mathbf{49}$$

Evaluating this directly via integer length loops takes $< 0.0001$ seconds.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Sample Pairs from Description
- $a = 7, n = 5 \implies 7^5 = 16\,807$ (5 digits).
- $a = 8, n = 9 \implies 8^9 = 134\,217\,728$ (9 digits).
- Both valid! Matches problem statement sample! $\checkmark$

### Example 2: Target Total Count
- Base 1: $1^1 \implies 1$
- Base 2: $2^1 \implies 1$
- Base 3: $3^1 \implies 1$
- Base 4: $4^1, 4^2 \implies 2$
- Base 5: $5^1, 5^2, 5^3 \implies 3$
- Base 6: $6^1 \dots 6^4 \implies 4$
- Base 7: $7^1 \dots 7^6 \implies 6$
- Base 8: $8^1 \dots 8^{10} \implies 10$
- Base 9: $9^1 \dots 9^{21} \implies 21$
- Total count:
  $$N_{\text{powers}} = 1 + 1 + 1 + 2 + 3 + 4 + 6 + 10 + 21 = \mathbf{49}$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **State Init** | `total_count = 0` | $\mathcal{O}(1)$ |
| **Stage 2** | **Base Loop** | For $a \in [1, 9]$ | $9$ iterations |
| **Stage 3** | **Exponent Loop** | While `len(str(a**n)) == n`: `total_count += 1, n += 1` | $\le 21$ steps |
| **Stage 4** | **Return Value** | Return scalar integer $49$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(1)$ | $\approx 0.0000$ seconds (49 checks total) |
| **Space Complexity** | $\mathcal{O}(1)$ | Scalar integer registers |
| **Dynamic Execution** | $100\%$ Inline | Logarithmic exponent bound iteration |

### Critical Invariants & Edge Cases Handled:
1. **$a \ge 10$ Proof**: Discarding $a \ge 10$ is mathematically rigorous since $10^n$ always has $n+1$ digits.
2. **Exact Equality**: Requires $\operatorname{len}(\operatorname{str}(a^n)) == n$, halting as soon as $a^n < 10^{n-1}$.
