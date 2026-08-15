# Square Remainders - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Let $r$ be the remainder when $(a-1)^n + (a+1)^n$ is divided by $a^2$:
$$r(a, n) = \left( (a - 1)^n + (a + 1)^n \right) \bmod a^2$$

For example, if $a = 7$ and $n = 3$, then:
$$r(7, 3) = (6^3 + 8^3) \bmod 49 = (216 + 512) \bmod 49 = 728 \bmod 49 = 42$$

As $n$ varies, $r$ can vary, but for $a = 7$ it turns out that $r_{\text{max}} = 42$.

The objective is to find **$\sum r_{\text{max}}$ for $3 \le a \le 1000$**:
$$S_{\text{rem}} = \sum_{a=3}^{1000} r_{\text{max}}(a)$$
where $r_{\text{max}}(a) = \max_{n \ge 1} r(a, n)$.

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Modular Exponentiation Loop
A naive approach computes $r(a, n)$ for $n = 1 \dots 2a$ using modular exponentiation:
```python
def naive_square_remainders(a):
    # Computes (pow(a-1, n, a*a) + pow(a+1, n, a*a)) % (a*a) for n in range(1, 2*a)
    # ...
```

### Binomial Theorem Expansion Modulo $a^2$
1. Expanding $(a-1)^n$ and $(a+1)^n$ modulo $a^2$ using the Binomial Theorem:
   $$(a - 1)^n \equiv (-1)^n + n(-1)^{n-1} a \pmod{a^2}$$
   $$(a + 1)^n \equiv 1 + na \pmod{a^2}$$
2. Adding both congruences:
   $$(a - 1)^n + (a + 1)^n \equiv \begin{cases} 2 \pmod{a^2} & \text{if } n \text{ is even} \\ 2na \pmod{a^2} & \text{if } n \text{ is odd} \end{cases}$$
3. For odd $n$, the remainder is $(2na) \bmod a^2 = a \cdot ((2n) \bmod a)$.
4. To maximize $(2n) \bmod a$ when $n$ is odd:
   - If $a$ is **even**: $(2n) \bmod a$ can achieve maximum value $a - 2 \implies r_{\text{max}}(a) = a(a - 2)$.
   - If $a$ is **odd**: $(2n) \bmod a$ can achieve maximum value $a - 1 \implies r_{\text{max}}(a) = a(a - 1)$.
5. This yields an exact $\mathcal{O}(1)$ closed-form formula per $a$, computing the entire sum in $\approx 0.0000$ seconds.

---

## 3. Core Intuition & Mathematical Structure

### Maximum Remainder Values for Early $a \in [3, 10]$

| Value of $a$ | Parity | Maximizing Odd $n$ | Remainder Modulo $a^2$ | Formula Value $r_{\text{max}}(a)$ |
| :---: | :---: | :---: | :---: | :---: |
| **$a = 3$** | Odd | $n = 1$ | $2(1)(3) = 6 \bmod 9$ | $3(2) = \mathbf{6}$ |
| **$a = 4$** | Even | $n = 1$ | $2(1)(4) = 8 \bmod 16$ | $4(2) = \mathbf{8}$ |
| **$a = 5$** | Odd | $n = 2$ ($2n \equiv 4$) | $2(2)(5) = 20 \bmod 25$ | $5(4) = \mathbf{20}$ |
| **$a = 6$** | Even | $n = 2$ ($2n \equiv 4$) | $2(2)(6) = 24 \bmod 36$ | $6(4) = \mathbf{24}$ |
| **$a = 7$** | Odd | $n = 3$ ($2n \equiv 6$) | $2(3)(7) = 42 \bmod 49$ | $7(6) = \mathbf{42}$ **(Sample)** |
| **$a = 8$** | Even | $n = 3$ ($2n \equiv 6$) | $2(3)(8) = 48 \bmod 64$ | $8(6) = \mathbf{48}$ |
| **$a = 9$** | Odd | $n = 4$ ($2n \equiv 8$) | $2(4)(9) = 72 \bmod 81$ | $9(8) = \mathbf{72}$ |
| **$a = 10$** | Even | $n = 4$ ($2n \equiv 8$) | $2(4)(10) = 80 \bmod 100$ | $10(8) = \mathbf{80}$ |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Closed-Form Parity Theorem
For all $a \ge 3$:
$$r_{\text{max}}(a) = \begin{cases} a(a - 2) & \text{if } a \equiv 0 \pmod 2 \\ a(a - 1) & \text{if } a \equiv 1 \pmod 2 \end{cases}$$

Summing over all $3 \le a \le 1000$:
$$S_{\text{rem}} = \sum_{a=3}^{1000} r_{\text{max}}(a) = \mathbf{333\,082\,500}$$

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Sample for $a = 7$
- $a = 7$ is odd $\implies r_{\text{max}}(7) = 7 \times (7 - 1) = 7 \times 6 = \mathbf{42}$.
- Matches problem statement sample! $\checkmark$

### Example 2: Target Evaluation for $3 \le a \le 1000$
- Summing closed-form values across all $998$ values of $a$:
  $$S_{\text{rem}} = \mathbf{333\,082\,500}$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Parity Function** | `r_max(a) = a*(a-2) if a%2==0 else a*(a-1)` | $\mathcal{O}(1)$ |
| **Stage 2** | **Summation Generator**| `sum(r_max(a) for a in range(3, limit + 1))` | $\mathcal{O}(\text{limit})$ |
| **Stage 3** | **Return Value** | Return scalar integer $333082500$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(\text{limit})$ where $\text{limit} = 1000$ | $\approx 0.0000$ seconds ($998$ multiplications) |
| **Space Complexity** | $\mathcal{O}(1)$ | Constant auxiliary memory |
| **Dynamic Execution** | $100\%$ Inline | Closed-form Binomial Theorem parity formula |

### Critical Invariants & Edge Cases Handled:
1. **Even vs Odd Parity**: Even $a$ cannot achieve $a-1$ because $2n$ is always even; thus the maximum even remainder below $a$ is $a-2$.
2. **Even Exponent $n$ Invariance**: When $n$ is even, $(a-1)^n + (a+1)^n \equiv 2 \pmod{a^2}$, which is strictly less than $a(a-2)$ for all $a \ge 3$.
