# Semidivisible Numbers - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

For an integer $n \ge 4$:
- $\operatorname{lps}(n)$ (lower prime square root) is the largest prime $\le \sqrt{n}$.
- $\operatorname{ups}(n)$ (upper prime square root) is the smallest prime $\ge \sqrt{n}$.

For example, $\operatorname{lps}(4) = 2 = \operatorname{ups}(4)$, $\operatorname{lps}(1000) = 31$, and $\operatorname{ups}(1000) = 37$.
An integer $n \ge 4$ is called **semidivisible** if exactly one of $\operatorname{lps}(n)$ and $\operatorname{ups}(n)$ divides $n$ (divisible by $\operatorname{lps}(n)$ XOR divisible by $\operatorname{ups}(n)$).

Examples:
- The semidivisible numbers $\le 15$ are $\{8, 10, 12\}$, with sum $8 + 10 + 12 = 30$ ($15$ is divisible by both $\operatorname{lps}(15)=3$ and $\operatorname{ups}(15)=5$, hence excluded).
- The sum of all $92$ semidivisible numbers up to $1000$ is $34\,825$.

Find the **sum of all semidivisible numbers not exceeding $999\,966\,663\,333$**.

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Individual Integer Scanning Bottlenecks
A naive algorithm iterates over $n \in [4, 10^{12}]$ computing integer square roots and prime bounds:
```python
def naive_semidivisible():
    # Iterating through 10^12 numbers takes > 500 hours
    # ...
```

### Analytical Interval Decomposition & Inclusion-Exclusion
1. **Prime Square Intervals:**
   For any consecutive prime pair $(p_1, p_2)$, all non-square integers $n \in (p_1^2, p_2^2)$ have:

$$
\operatorname{lps}(n) = p_1, \quad \operatorname{ups}(n) = p_2
$$

2. **Inclusion-Exclusion within Interval $[L, R]$:**
   Let $[L, R] = [p_1^2 + 1, \min(p_2^2 - 1, \text{limit})]$.
   - Sum of multiples of $p_1$: $S(p_1, L, R)$
   - Sum of multiples of $p_2$: $S(p_2, L, R)$
   - Sum of multiples of $p_1 p_2$: $S(p_1 p_2, L, R)$
   The contribution of semidivisible numbers in $[L, R]$ is:

$$
\Delta \text{Sum} = S(p_1, L, R) + S(p_2, L, R) - 2 S(p_1 p_2, L, R)
$$

3. **$\mathcal{O}(1)$ Closed-Form Arithmetic Series:**
   The sum of multiples of $k$ in $[L, R]$ with start $a = \lceil L/k \rceil k$ and end $b = \lfloor R/k \rfloor k$ is:

$$
S(k, L, R) = \frac{\text{cnt} \cdot (a + b)}{2}, \quad \text{where } \text{cnt} = \frac{b - a}{k} + 1
$$

---

## 3. Core Intuition & Mathematical Structure

### Arithmetic Progression Sums on Sample Interval $(2^2, 3^2) = (4, 9)$ and $(3^2, 5^2) = (9, 25)$

| Interval $(p_1^2, p_2^2)$ | Range $[L, R]$ | Multiples of $p_1$ (Sum $S_1$) | Multiples of $p_2$ (Sum $S_2$) | Multiples of $p_1 p_2$ (Sum $S_{12}$) | Semidivisible Sum $S_1 + S_2 - 2 S_{12}$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **$(2^2, 3^2) = (4, 9)$** | $[5, 8]$ | $\{6, 8\} \implies 14$ | $\{6\} \implies 6$ | $\{6\} \implies 6$ | $14 + 6 - 2(6) = \mathbf{8}$ |
| **$(3^2, 5^2) = (9, 25)$** | $[10, 24]$ | $\{12, 15, 18, 21, 24\} \implies 90$ | $\{10, 15, 20\} \implies 45$ | $\{15\} \implies 15$ | $90 + 45 - 2(15) = \mathbf{105}$ |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Master Arithmetic Sieve Algorithm
```python
def solve(limit: int = 999966663333) -> int:
    primes = sieve_primes(math.isqrt(limit) + 1000)
    total_sum = 0

    for idx in range(len(primes) - 1):
        p1, p2 = primes[idx], primes[idx + 1]
        L = p1 * p1 + 1
        R = min(p2 * p2 - 1, limit)
        if L > R:
            if p1 * p1 > limit:
                break
            continue

        s1 = sum_multiples(p1, L, R)
        s2 = sum_multiples(p2, L, R)
        s12 = sum_multiples(p1 * p2, L, R)

        total_sum += s1 + s2 - 2 * s12
        if p1 * p1 >= limit:
            break

    return total_sum
```

Evaluating for $\text{limit} = 999\,966\,663\,333$:

$$
\text{Sum} = \mathbf{1\,259\,187\,438\,574\,927\,161}
$$

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Sample Verification for $\text{limit} = 15$
- Interval $(2^2, 3^2) = [5, 8]$: Semidivisible $\{8\} \implies 8$.
- Interval $(3^2, 5^2) = [10, 15]$:
  - Multiples of 3: $\{12, 15\} \implies 27$.
  - Multiples of 5: $\{10, 15\} \implies 25$.
  - Multiple of 15: $\{15\} \implies 15$.
  - Sum: $27 + 25 - 2(15) = 22$ (numbers $\{10, 12\}$).
- Total: $8 + 22 = \mathbf{30}$.
- Matches problem statement sample! $\checkmark$

### Example 2: Sample Verification for $\text{limit} = 1000$
- Sum across intervals up to $p_1 = 31, p_2 = 37$:

$$
\text{Total Sum} = \mathbf{34\,825} \quad (\checkmark)
$$

### Example 3: Target Evaluation for $\text{limit} = 999\,966\,663\,333$
- Sum across all consecutive prime pairs up to $\sqrt{N} \approx 10^6$:

$$
\text{Total Sum} = \mathbf{1\,259\,187\,438\,574\,927\,161}
$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Prime Sieve** | Sieve all primes $p \le \sqrt{\text{limit}} + 1000$ | $\mathcal{O}(\sqrt{N} \log \log \sqrt{N})$ |
| **Stage 2** | **Pair Iteration** | Loop consecutive prime pairs $(p_1, p_2)$ | $\mathcal{O}(\pi(\sqrt{N}))$ |
| **Stage 3** | **Interval Bounds**| $L = p_1^2 + 1, R = \min(p_2^2 - 1, \text{limit})$ | $\mathcal{O}(1)$ |
| **Stage 4** | **Inclusion-Exclusion**| $S(p_1) + S(p_2) - 2 S(p_1 p_2)$ | $\mathcal{O}(1)$ |
| **Stage 5** | **Accumulate** | `total_sum += delta_sum` | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(\pi(\sqrt{N})) \approx 78\,498$ iterations | $\approx 0.10$ seconds |
| **Space Complexity** | $\mathcal{O}(\sqrt{N})$ | Prime bytearray $\approx 1$ MB |
| **Dynamic Execution** | $100\%$ Inline | Closed-form arithmetic series inclusion-exclusion |

### Critical Invariants & Edge Cases Handled:
1. **Truncated Interval at Limit**: The upper bound $R = \min(p_2^2 - 1, \text{limit})$ cleanly handles the final boundary interval.
2. **Exclusion of Square Endpoints**: $L = p_1^2 + 1$ and $R = p_2^2 - 1$ strictly exclude perfect squares where $\operatorname{lps}(n) = \operatorname{ups}(n)$.