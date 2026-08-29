# Reciprocal Cycles - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

A unit fraction $\frac{1}{d}$ for an integer $d \ge 2$ has a decimal representation:

$$
\frac{1}{d} = 0.a_1 a_2 \dots a_k (r_1 r_2 \dots r_\lambda)^\infty
$$

where $\lambda(d) \in \mathbb{N}_0$ denotes the length of the recurring decimal cycle.

The objective is to find the value of $d < 1000$ for which $\frac{1}{d}$ contains the longest recurring cycle:

$$
d_{\text{max}} = \operatorname*{arg\,max}_{2 \le d < 1000} \lambda(d)
$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Unbounded Ascending Search
A naive algorithm performs long division on all integers $d \in [2, 999]$ in ascending order:
```python
def naive_longest_cycle(limit):
    best_d, max_len = 0, 0
    for d in range(2, limit):
        # tests all 1000 denominators without pruning
        # ...
```

### Computational Inefficiencies
1. **Testing Small Denominators**: Denominators $d < 100$ cannot produce cycle lengths exceeding $100$.
2. **Descending Order Superiority**: Since $\lambda(d) \le d - 1$, searching in descending order from $999$ downwards enables immediate termination as soon as $d \le \lambda_{\text{max}}$.

---

## 3. Core Intuition & Mathematical Structure

For any integer $d$ coprime to 10 ($\gcd(d, 10) = 1$), the period length $\lambda(d)$ equals the multiplicative order of $10$ modulo $d$:

$$
\lambda(d) = \operatorname{ord}_d(10) = \min \{ k \ge 1 \mid 10^k \equiv 1 \pmod d \}
$$

By Euler's Totient Theorem:

$$
\lambda(d) \le \varphi(d) \le d - 1
$$

When $d$ is a prime and $10$ is a primitive root modulo $d$, $\lambda(d) = d - 1$ (Full Reptend Prime).

### Reciprocal Unit Fractions & Period Length Table

| Denominator $d$ | Decimal Expansion of $1/d$ | Recurring Block | Period Length $\lambda(d)$ | Maximum Possible $d - 1$ |
| :---: | :--- | :---: | :---: | :---: |
| **$2$** | $0.5$ | — | $0$ | $1$ |
| **$3$** | $0.(3)$ | `3` | $1$ | $2$ |
| **$6$** | $0.1(6)$ | `6` | $1$ | $5$ |
| **$7$** | $0.(142857)$ | `142857` | **$6$** | $6$ (Full Reptend) |
| **$11$** | $0.(09)$ | `09` | $2$ | $10$ |
| **$13$** | $0.(076923)$ | `076923` | $6$ | $12$ |
| **$983$** | $0.(001017\dots)$ | $982$-digit block | **$982$** | $982$ (Full Reptend) |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Descending Pruning Bound
1. Let $\lambda_{\text{max}}$ be the maximum recurring period discovered so far.
2. If we test candidate $d$ in descending order from $999$ downwards:

$$
\lambda(d) \le d - 1 < d
$$

3. As soon as $d \le \lambda_{\text{max}}$, no remaining divisor $d' \le d$ can ever exceed $\lambda_{\text{max}}$.
4. When $d = 983$ is evaluated, $\lambda(983) = 982$.
5. The next candidate is $d = 982 \le 982 = \lambda_{\text{max}}$, halting the search immediately after only $17$ candidate evaluations!

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Evaluation for $d = 7$
- Long division remainders starting at $r_0 = 1$:
  - Step 1: $10 \times 1 = 10 \equiv 3 \pmod 7$ (Pos 0: Rem 1)
  - Step 2: $10 \times 3 = 30 \equiv 2 \pmod 7$ (Pos 1: Rem 3)
  - Step 3: $10 \times 2 = 20 \equiv 6 \pmod 7$ (Pos 2: Rem 2)
  - Step 4: $10 \times 6 = 60 \equiv 4 \pmod 7$ (Pos 3: Rem 6)
  - Step 5: $10 \times 4 = 40 \equiv 5 \pmod 7$ (Pos 4: Rem 4)
  - Step 6: $10 \times 5 = 50 \equiv 1 \pmod 7$ (Pos 5: Rem 5)
  - Step 7: Remainder $1$ reappears at Pos 6!
- Cycle length: $6 - 0 = \mathbf{6}$. Matches sample! $\checkmark$

### Example 2: Target Evaluation for $d < 1000$
- Descending scan evaluates $d = 999, 998, \dots, 983$.
- At $d = 983$ (prime): $\lambda(983) = 982$.
- Pruning terminates at $d = 982$.
- Denominator with Longest Cycle: $d = \mathbf{983}$.

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **State Tracking** | Set $\lambda_{\text{max}} = 0, \text{best\_d} = 0$ | $\mathcal{O}(1)$ |
| **Stage 2** | **Descending Search** | For $d \in [999, 2]$ step $-1$: if $d \le \lambda_{\text{max}}$, `break` | $\le 17$ steps |
| **Stage 3** | **Remainder Tracking** | Loop `rem = (rem * 10) % d` with dictionary lookup | $\mathcal{O}(d)$ |
| **Stage 4** | **Max Cycle Update** | If $\text{length} > \lambda_{\text{max}}$: update peak | $\mathcal{O}(1)$ |
| **Stage 5** | **Return Value** | Return scalar integer $983$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N^2)$ pruned to $\approx 17$ divisor tests | $\approx 0.001$ seconds |
| **Space Complexity** | $\mathcal{O}(N)$ | Remainder dictionary $\approx 10$ KB |
| **Dynamic Execution** | $100\%$ Inline | Modulo 10 remainder tracking |

### Critical Invariants & Edge Cases Handled:
1. **Terminating Decimals**: If $\text{rem} == 0$ (e.g. for powers of 2 and 5), the function returns 0.
2. **Descending Early Break**: Condition $d \le \lambda_{\text{max}}$ guarantees optimality because $\lambda(d') \le d' - 1 < d \le \lambda_{\text{max}}$.