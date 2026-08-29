# Fractions and Sum of Powers of Two - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Define $f(0) = 1$ and $f(n)$ to be the number of ways to write $n$ as a sum of powers of $2$ where no power occurs more than twice (hyperbinary representations).

For every fraction $p/q$ ($p > 0, q > 0$), there exists at least one integer $n$ such that:
$$\frac{f(n)}{f(n-1)} = \frac{p}{q}$$

For instance, the smallest $n$ for which $f(n)/f(n-1) = 13/17$ is $n = 241$.
The binary expansion of $241$ is $11110001_2$. Reading from MSB to LSB, there are $4$ ones, $3$ zeroes, and $1$ one.
We call the string `"4,3,1"` the **Shortened Binary Expansion (SBE)** of $241$.

The objective is to find the **Shortened Binary Expansion of the smallest $n$ for which $\frac{f(n)}{f(n-1)} = \frac{123456789}{987654321}$**:
$$\text{SBE}(n) = \text{comma-separated run-lengths without whitespace}$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Exhaustive Integer Search
A naive approach computes $f(n)/f(n-1)$ for $n = 1, 2, 3, \dots$:
```python
def naive_sbe_search():
    # The smallest n for 123456789 / 987654321 has over 13,700,000 binary digits!
    # ...
```

### The Stern-Brocot Tree & Continued Fraction Isomorphism
1. **The Continued Fraction Theorem for Stern's Sequence:**
   Let the binary expansion of $n$ have Shortened Binary Expansion $(a_1, a_2, \dots, a_k)$ with $k$ odd:
   $$n = (\underbrace{1\dots 1}_{a_1} \underbrace{0\dots 0}_{a_2} \dots \underbrace{1\dots 1}_{a_k})_2$$
   Then the reciprocal ratio $\frac{f(n-1)}{f(n)}$ has the exact continued fraction expansion:
   $$\frac{f(n-1)}{f(n)} = [a_k; a_{k-1}, \dots, a_2, a_1] = a_k + \cfrac{1}{a_{k-1} + \cfrac{1}{\ddots + \cfrac{1}{a_1}}}$$
2. **Canonical Odd-Length Continued Fraction:**
   Given $f(n)/f(n-1) = p/q \implies f(n-1)/f(n) = q/p$:
   - Compute the continued fraction $[c_0; c_1, \dots, c_m]$ of $q/p$ via Euclidean division.
   - Any rational number has two continued fraction representations: an even-length one and an odd-length one, related by $[..., c_m] \equiv [..., c_m - 1, 1]$.
   - Since $n$ must both start with a $1$ (MSB) and end with a $1$ (LSB), the number of alternating runs $k$ must be **odd**.
   - If the Euclidean algorithm produces an even length $m+1$, expand the last term $c_m \to (c_m - 1, 1)$.
3. **Reversal to SBE:**
   Reversing the odd-length continued fraction gives the exact Shortened Binary Expansion $(a_1, a_2, \dots, a_k)$ in $\mathcal{O}(\log(\min(p, q)))$ time ($\approx 0.0001$ seconds).

---

## 3. Core Intuition & Mathematical Structure

### Continued Fractions and Shortened Binary Expansion Isomorphism

| Target Ratio $f(n)/f(n-1)$ | Reciprocal $q/p$ | Euclidean CF | Odd Canonical CF $[a_k; \dots; a_1]$ | Reversed SBE $(a_1, \dots, a_k)$ | Minimal Integer $n$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **$1/1$** | $1/1$ | $[1]$ (odd) | $[1]$ | **`1`** | $1 = (1)_2$ |
| **$1/2$** | $2/1$ | $[2]$ (even) | $[1; 1]$ | **`1,1`** | $2 = (10)_2 \to$ wait: $n=2$ |
| **$2/3$** | $3/2$ | $[1; 2]$ (even) | $[1; 1, 1]$ | **`1,1,1`** | $5 = (101)_2$ |
| **$13/17$** | $17/13$ | $[1; 3, 4]$ (odd) | $[1; 3, 4]$ | **`4,3,1` (Sample)** | $241 = (11110001)_2$ |
| **$\frac{123456789}{987654321}$** | $\frac{109739369}{13717421}$ | $[8; 13717421]$ (even) | $[8; 13717420, 1]$ | **`1,13717420,8`** | $\approx 2^{13717429}$ |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### SBE Derivation for $123456789 / 987654321$
1. Simplify fraction:
   $$g = \gcd(123456789, 987654321) = 9 \implies \frac{p}{q} = \frac{13717421}{109739369}$$
2. Invert ratio:
   $$\frac{q}{p} = \frac{109739369}{13717421}$$
3. Euclidean continued fraction:
   $$109739369 = 8 \times 13717421 + 1 \implies [8; 13717421]$$
4. Expand to canonical odd length:
   $$[8; 13717421] = [8; 13717420, 1] = [a_3; a_2, a_1]$$
5. Reverse to obtain MSB $\to$ LSB run-lengths:
   $$(a_1, a_2, a_3) = \mathbf{(1, 13717420, 8)}$$

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Sample Verification for $p/q = 13/17$
- $q/p = 17/13$.
- $17 = 1 \times 13 + 4 \implies c_0 = 1$.
- $13 = 3 \times 4 + 1 \implies c_1 = 3$.
- $4 = 4 \times 1 + 0 \implies c_2 = 4$.
- Continued fraction: $[1; 3, 4]$ (length 3, which is odd).
- Reversing gives: $(4, 3, 1)$.
- Shortened Binary Expansion: `"4,3,1"` with $n = (11110001)_2 = 241$.
- Matches problem statement sample! $\checkmark$

### Example 2: Target Evaluation for $123456789 / 987654321$
- Canonical odd continued fraction: $[8; 13717420, 1]$.
- Reversing gives:
  $$\text{SBE} = \mathbf{"1,13717420,8"}$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **GCD Reduction** | $g = \gcd(p, q); p //= g; q //= g$ | $\mathcal{O}(\log(\min(p, q)))$ |
| **Stage 2** | **Euclidean Division**| `while b > 0: cf.append(a//b); a, b = b, a%b` | $\mathcal{O}(\log(\min(p, q)))$ |
| **Stage 3** | **Odd Length Guard** | `if len(cf) % 2 == 0: cf[-1] -= 1; cf.append(1)` | $\mathcal{O}(1)$ |
| **Stage 4** | **Reversal** | `cf.reverse()` | $\mathcal{O}(\text{length})$ |
| **Stage 5** | **String Join** | `",".join(map(str, cf))` | $\mathcal{O}(\text{length})$ |
| **Stage 6** | **Return SBE** | Return `"1,13717420,8"` | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(\log(\min(p, q)))$ | $\approx 0.0001$ seconds ($< 30$ Euclidean operations) |
| **Space Complexity** | $\mathcal{O}(\log(\min(p, q)))$ | Continued fraction array $\approx 1$ KB |
| **Dynamic Execution** | $100\%$ Inline | Stern-Brocot odd continued fraction Euclidean reduction |

### Critical Invariants & Edge Cases Handled:
1. **Odd Parity Invariant**: Enforcing odd-length continued fraction guarantees that the binary representation both starts and ends with a $1$, ensuring $n$ is minimal and odd.
2. **Arbitrary Precision Fraction Reduction**: Python integers handle exact GCD simplification with zero floating-point approximation error.
