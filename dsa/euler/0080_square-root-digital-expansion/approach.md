# Square Root Digital Expansion - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

It is well known that if the square root of a natural number is not an integer, then it is irrational.
The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is:
$$\sqrt{2} = 1.41421356237309504880\dots$$
The digital sum of the first one hundred ($100$) decimal digits of $\sqrt{2}$ is $475$.

For the first one hundred natural numbers ($1 \le n \le 100$), there are 10 perfect squares ($1, 4, 9, 16, 25, 36, 49, 64, 81, 100$) and 90 irrational square roots.

The objective is to find the total of the digital sums of the first one hundred decimal digits for all **irrational square roots** up to $100$:
$$S_{\text{total}} = \sum_{\substack{1 \le n \le 100 \\ \lfloor \sqrt{n} \rfloor^2 \neq n}} \left( \sum_{i=1}^{100} d_i(\sqrt{n}) \right)$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Floating-Point Inaccuracies
A naive algorithm uses standard floating-point operations (`math.sqrt` or `float`):
```python
def naive_sqrt_expansion(n):
    # Standard float64 gives at most 15-17 significant digits!
    # ...
```

### Exact BigInt Integer Scaling
1. To extract the first $D = 100$ decimal digits of $\sqrt{n}$ without floating-point precision loss:
   $$\lfloor \sqrt{n} \cdot 10^{D-1} \rfloor = \lfloor \sqrt{n \cdot 10^{2(D-1)}} \rfloor = \operatorname{isqrt}\left( n \times 10^{2 \times 99} \right)$$
2. The scaled integer square root $\operatorname{isqrt}(n \times 10^{198})$ is an exact 100-digit BigInt integer whose digits correspond 1-to-1 with the leading 100 digits of $\sqrt{n}$.
3. Using `math.isqrt`, all 90 irrational roots evaluate in $\approx 0.002$ seconds.

---

## 3. Core Intuition & Mathematical Structure

### Scaled Integer Square Root Extraction for Early Irrational Roots

| Integer $n$ | Scaled Expression $n \times 10^{198}$ | Leading Digits $\operatorname{isqrt}(n \times 10^{198})$ | 100-Digit Digital Sum $S(n)$ |
| :---: | :--- | :--- | :---: |
| **$2$** | $2 \times 10^{198}$ | `141421356237309504880...` | **$475$ (Sample)** |
| **$3$** | $3 \times 10^{198}$ | `173205080756887729352...` | $441$ |
| **$4$** | $4 \times 10^{198}$ | Perfect Square ($\sqrt{4}=2$) | Skipped (Rational) |
| **$5$** | $5 \times 10^{198}$ | `223606797749978969640...` | $437$ |
| **$6$** | $6 \times 10^{198}$ | `244948974278317809819...` | $461$ |
| **$7$** | $7 \times 10^{198}$ | `264575131106459059050...` | $418$ |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Extraction & Summation Pipeline
1. Multiplier: $\text{scale} = 10^{2 \times (100 - 1)} = 10^{198}$.
2. Initialize $S_{\text{total}} = 0$.
3. For $n = 1 \dots 100$:
   - Let $r = \lfloor \sqrt{n} \rfloor$.
   - If $r \times r == n$: continue (skip perfect squares).
   - Compute BigInt root: $R = \operatorname{isqrt}(n \times 10^{198})$.
   - Convert to string `s = str(R)[:100]`.
   - $S_{\text{total}} += \sum_{c \in s} \operatorname{int}(c)$.
4. Return $S_{\text{total}}$.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Trace for $n = 2$
- $R_2 = \operatorname{isqrt}(2 \times 10^{198})$.
- $R_2 = 1414213562373095048801688724209698078569671875376948073176679737990732478462107038850387534327641572$.
- Summing these 100 digits:
  $$S(2) = 1 + 4 + 1 + 4 + 2 + \dots + 7 + 2 = \mathbf{475}$$
- Matches problem statement sample! $\checkmark$

### Example 2: Target Evaluation across 90 Irrational Roots ($n \le 100$)
- Summing digital expansions for all 90 non-squares:
  $$S_{\text{total}} = \mathbf{40\,886}$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Scale Init** | `scale = 10 ** (2 * (digits - 1))` ($10^{198}$) | $\mathcal{O}(1)$ |
| **Stage 2** | **Loop $n \in [1, 100]$** | If `isqrt(n)**2 == n: continue` | $100$ iterations |
| **Stage 3** | **BigInt Square Root** | `big_root = math.isqrt(n * scale)` | Newton-Raphson |
| **Stage 4** | **Digit Summation** | `sum(int(c) for c in str(big_root)[:100])` | $100$ characters |
| **Stage 5** | **Return Total** | Return scalar integer $40886$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N \cdot D)$ where $N = 100, D = 100$ | $\approx 0.002$ seconds |
| **Space Complexity** | $\mathcal{O}(D)$ | 100-digit string buffer $\approx 1$ KB |
| **Dynamic Execution** | $100\%$ Inline | Exact integer scaling square root extraction |

### Critical Invariants & Edge Cases Handled:
1. **Rational Root Exclusion**: Perfectly filters out the 10 squares ($1, 4, 9, \dots, 100$) via exact square check `root * root == n`.
2. **Exact 100-Digit Alignment**: Multiplier $10^{198}$ guarantees that taking the first 100 characters of `str(big_root)` includes the integer part and the first 99 decimal fraction digits, totaling exactly 100 digits.
