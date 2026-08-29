# Combinatoric Selections - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Let $\binom{n}{r}$ denote the binomial coefficient (the number of combinations of $n$ items chosen $r$ at a time):
$$\binom{n}{r} = \frac{n!}{r!(n - r)!} \quad \text{for } 0 \le r \le n$$

The objective is to find how many values of $\binom{n}{r}$ for $1 \le n \le 100$ are strictly greater than one million ($1\,000\,000$):
$$N_{\text{exceed}} = \sum_{n=1}^{100} \sum_{r=1}^n \mathbb{I}\left( \binom{n}{r} > 1\,000\,000 \right)$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Exhaustive Evaluation of All Pairs
A naive algorithm calculates all $\sum_{n=1}^{100} n = 5050$ combinations individually:
```python
def naive_combinatoric_selections():
    # checks all 5050 pairs (n, r)
    # ...
```

### Unimodal Symmetry Theorem
1. For any fixed $n$, the sequence of binomial coefficients $\left\{ \binom{n}{r} \right\}_{r=0}^n$ is symmetric:
   $$\binom{n}{r} = \binom{n}{n - r}$$
2. The sequence is strictly unimodal, increasing monotonically for $r \le \lfloor n/2 \rfloor$ and decreasing for $r > \lfloor n/2 \rfloor$.
3. **Theorem:** If $r_{\text{min}}$ is the smallest integer $r \le \lfloor n/2 \rfloor$ such that $\binom{n}{r_{\text{min}}} > 1\,000\,000$, then:
   $$\binom{n}{r} > 1\,000\,000 \quad \forall r \in [r_{\text{min}}, n - r_{\text{min}}]$$
   The exact count of exceeding values in row $n$ is:
   $$\text{Count}(n) = n - 2 r_{\text{min}} + 1$$

---

## 3. Core Intuition & Mathematical Structure

### Unimodal Central Peak for Small $n$

| Row $n$ | Smallest $r$ with $\binom{n}{r} > 10^6$ | Central Exceeding Range $[r, n-r]$ | Exceeding Count $n - 2r + 1$ |
| :---: | :---: | :---: | :---: |
| **$n \le 22$** | None ($\binom{22}{11} = 705\,432 < 10^6$) | $\emptyset$ | $0$ |
| **$n = 23$** | $r = 10$ ($\binom{23}{10} = 1\,144\,066$) | $[10, 13]$ | $23 - 2(10) + 1 = \mathbf{4}$ |
| **$n = 24$** | $r = 9$ ($\binom{24}{9} = 1\,307\,504$) | $[9, 15]$ | $24 - 2(9) + 1 = \mathbf{7}$ |
| **$n = 25$** | $r = 8$ ($\binom{25}{8} = 1\,081\,575$) | $[8, 17]$ | $25 - 2(8) + 1 = \mathbf{10}$ |
| **$n = 100$** | $r = 4$ ($\binom{100}{4} = 3\,921\,225$) | $[4, 96]$ | $100 - 2(4) + 1 = \mathbf{93}$ |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Symmetry-Accelerated Row Scanning
For each $n \in [1, 100]$:
1. Scan $r = 1, 2, \dots, \lfloor n/2 \rfloor$.
2. Compute $\binom{n}{r}$ using `math.comb(n, r)`.
3. As soon as $\binom{n}{r} > 1\,000\,000$:
   - Add $n - 2r + 1$ directly to total counter.
   - Break inner loop immediately (skipping the remainder of row $n$).
4. Total additions are performed in $\approx 0.0001$ seconds.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Trace for Row $n = 23$
- Scanning $r = 1 \dots 11$:
  - $\binom{23}{1} = 23$
  - $\dots$
  - $\binom{23}{9} = 817\,190 < 10^6$
  - $\binom{23}{10} = \mathbf{1\,144\,066} > 10^6$
- $r_{\text{min}} = 10$.
- Range of values exceeding $10^6$: $r \in [10, 13] \implies \{10, 11, 12, 13\}$.
- Count: $23 - 2(10) + 1 = 23 - 20 + 1 = \mathbf{4}$. Matches problem statement sample! $\checkmark$

### Example 2: Target Evaluation for $1 \le n \le 100$
- Summing counts for $n = 23 \dots 100$:
  $$N_{\text{exceed}} = \mathbf{4075}$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **State Setup** | `total_count = 0` | $\mathcal{O}(1)$ |
| **Stage 2** | **Row Loop** | For $n \in [1, 100]$ | $100$ rows |
| **Stage 3** | **Symmetry Scan** | For $r \in [1, n//2]$: if `math.comb(n, r) > 10**6` | $\le 50$ checks per row |
| **Stage 4** | **Symmetry Addition** | `total_count += n - 2*r + 1; break` | $\mathcal{O}(1)$ |
| **Stage 5** | **Return Total** | Return scalar integer $4075$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N^2)$ pruned to $\approx 500$ checks | $\approx 0.0001$ seconds for $N = 100$ |
| **Space Complexity** | $\mathcal{O}(1)$ | Scalar integer registers |
| **Dynamic Execution** | $100\%$ Inline | Unimodal symmetry range accumulation |

### Critical Invariants & Edge Cases Handled:
1. **$n < 23$ Skip**: Rows with no values exceeding $10^6$ naturally execute without triggering additions.
2. **Central Element Parity**: Formula $n - 2r + 1$ correctly accounts for odd and even row lengths without off-by-one errors.
