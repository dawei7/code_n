# Digit Cancelling Fractions - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Let $\mathcal{F}$ denote the set of all fractions strictly less than 1 formed by two-digit numerators and denominators:
$$\mathcal{F} = \left\{ \frac{a}{b} \;\middle|\; 10 \le a < b \le 99 \right\}$$

A fraction $\frac{a}{b} \in \mathcal{F}$ is defined as a **non-trivial digit-cancelling fraction** if:
1. $a \not\equiv 0 \pmod{10}$ or $b \not\equiv 0 \pmod{10}$ (excluding trivial multiples of 10 such as $\frac{30}{50} = \frac{3}{5}$).
2. The decimal representations of $a$ and $b$ share a common non-zero digit $d \in \{1, 2, \dots, 9\}$.
3. Cancelling that common digit $d$ leaves remaining single-digit integers $c, e$ such that:
$$\frac{a}{b} = \frac{c}{e}$$

The objective is to find the denominator of the product of the four non-trivial fractions when reduced to lowest terms.

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Floating-Point Comparison
A naive approach uses floating-point division `a / b == c / e`:
```python
# Susceptible to IEEE 754 precision issues
```

### Exact Cross-Multiplication Principle
1. Two rational fractions $\frac{a}{b} = \frac{c}{e}$ are equal if and only if their integer cross-product matches:
   $$a \cdot e = b \cdot c$$
2. The search domain is finite with only $\binom{90}{2} = 4005$ total fraction pairs, easily searchable in $\approx 0.001$ seconds.

---

## 3. Core Intuition & Mathematical Structure

### The Four Non-Trivial Fractions Table

| Fraction $\frac{a}{b}$ | Common Digit $d$ | Cancelled Fraction $\frac{c}{e}$ | Cross-Multiplication $a \cdot e = b \cdot c$ | Lowest Terms Value |
| :---: | :---: | :---: | :---: | :---: |
| $\mathbf{\frac{16}{64}}$ | $6$ | $\frac{1}{4}$ | $16 \times 4 = 64 \times 1 = \mathbf{64}$ | $\frac{1}{4}$ |
| $\mathbf{\frac{19}{95}}$ | $9$ | $\frac{1}{5}$ | $19 \times 5 = 95 \times 1 = \mathbf{95}$ | $\frac{1}{5}$ |
| $\mathbf{\frac{26}{65}}$ | $6$ | $\frac{2}{5}$ | $26 \times 5 = 65 \times 2 = \mathbf{130}$ | $\frac{2}{5}$ |
| $\mathbf{\frac{49}{98}}$ | $9$ | $\frac{4}{8}$ | $49 \times 8 = 98 \times 4 = \mathbf{392}$ | $\frac{1}{2}$ |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Product Reduction to Lowest Terms
Multiplying all four non-trivial fractions together:
$$\prod_{i=1}^4 \frac{a_i}{b_i} = \frac{16}{64} \times \frac{19}{95} \times \frac{26}{65} \times \frac{49}{98} = \frac{1}{4} \times \frac{1}{5} \times \frac{2}{5} \times \frac{1}{2}$$
$$= \frac{1 \times 1 \times 2 \times 1}{4 \times 5 \times 5 \times 2} = \frac{2}{200} = \mathbf{\frac{1}{100}}$$

The greatest common divisor is $\gcd(2, 200) = 2$.
Dividing numerator and denominator by $\gcd$:
$$\text{Simplified Denominator} = \frac{200}{2} = \mathbf{100}$$

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Trace for Fraction $\frac{49}{98}$
- Numerator $a = 49$, denominator $b = 98$.
- Common digit: `9`.
- Cancelling `9`: $c = 4$, $e = 8$.
- Cross-multiplication check: $49 \times 8 = 392$, and $98 \times 4 = 392$.
- Because $392 = 392$, the cancellation is valid! $\checkmark$

### Example 2: Target Evaluation
- Product numerator: $16 \times 19 \times 26 \times 49 = 387\,296$.
- Product denominator: $64 \times 95 \times 65 \times 98 = 38\,729\,600$.
- $\gcd(387296, 38729600) = 387296$.
- Reduced denominator:
  $$\text{Denominator} = \frac{38\,729\,600}{387\,296} = \mathbf{100}$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Scan Fraction Domain** | For $a \in [10, 98], b \in [a+1, 99]$ | $4005$ checks |
| **Stage 2** | **Filter Trivial Zeros** | If $a \equiv 0 \land b \equiv 0 \pmod{10}$, skip | $\mathcal{O}(1)$ |
| **Stage 3** | **Common Digit Test** | For $d \in \text{set}(a) \cap \text{set}(b)$: test $a \cdot e == b \cdot c$ | $\mathcal{O}(1)$ |
| **Stage 4** | **Accumulate Products** | `num_prod *= a; den_prod *= b` | $\mathcal{O}(1)$ |
| **Stage 5** | **GCD Reduction** | `den_prod // math.gcd(num_prod, den_prod)` | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(1)$ | $\approx 0.001$ seconds for $4005$ fraction pairs |
| **Space Complexity** | $\mathcal{O}(1)$ | Constant integer registers |
| **Dynamic Execution** | $100\%$ Inline | Cross-multiplication and Euclidean GCD |

### Critical Invariants & Edge Cases Handled:
1. **Division by Zero Protection**: Ensures remaining denominator string $e \neq \text{"0"}$.
2. **Proper Fraction Ordering**: Constraint $a < b$ ensures only fractions strictly less than 1 are processed.
