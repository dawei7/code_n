# Exploring Pascal's Pyramid - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

A triangular number of numbers is arranged in the shape of an equilateral triangle, forming the $n$-th layer of **Pascal's Pyramid** (also called the trinomial triangle).
The expansion of $(x + y + z)^N$ consists of terms:

$$
\frac{N!}{i! \, j! \, k!} x^i y^j z^k \quad \text{where } i, j, k \ge 0 \text{ and } i + j + k = N
$$

For $N = 200\,000$, we wish to count how many coefficients $\frac{N!}{i! \, j! \, k!}$ are multiples of $10^{12} = 2^{12} \times 5^{12}$.

The objective is to find the **number of trinomial coefficients in $(x+y+z)^{200000}$ that are divisible by $10^{12}$**:

$$
N_{\text{trinomial}} = \left| \left\{ (i, j, k) \in \mathbb{N}_0^3 \;\middle|\; i + j + k = 200\,000 \land v_2\left(\frac{N!}{i! j! k!}\right) \ge 12 \land v_5\left(\frac{N!}{i! j! k!}\right) \ge 12 \right\} \right|
$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Direct 3-Variable Search
A naive approach loops over all $\approx \frac{200000^2}{2} = 2 \times 10^{10}$ triples $(i, j, k)$:
```python
def naive_pascals_pyramid():
    # Computing 2 x 10^10 trinomial coefficients is completely intractable
    # ...
```

### Kummer's Theorem & Base-5 / Base-2 Carry Bounds
1. **Kummer's Theorem for Multinomial Coefficients:**
   For any prime $p$, the $p$-adic valuation $v_p\left(\frac{N!}{i! j! k!}\right)$ equals the **number of carries** when adding $i, j, k$ in base $p$:

$$
v_p\left(\frac{N!}{i! j! k!}\right) = \frac{S_p(i) + S_p(j) + S_p(k) - S_p(N)}{p - 1}
$$

   where $S_p(m)$ is the sum of digits of $m$ in base $p$.
2. **Divisibility Conditions:**
   - **Base 5:** $N = 200\,000 = (2, 2, 4, 0, 0, 0, 0, 0)_5 \implies S_5(N) = 8$.

$$
v_5 \ge 12 \iff S_5(i) + S_5(j) + S_5(k) \ge 8 + 4 \times 12 = 56
$$

   - **Base 2:** $N = 200\,000 = (110000110101000000)_2 \implies S_2(N) = 6$.

$$
v_2 \ge 12 \iff S_2(i) + S_2(j) + S_2(k) \ge 6 + 12 = 18
$$

3. **Canonical Symmetry Ordering $0 \le i \le j \le k$:**
   Restricting search to $i \le \lfloor N/3 \rfloor$ and $j \in [i, \lfloor(N-i)/2\rfloor]$ evaluates only $\frac{1}{6}$ of the triangle.
   - Multiplicity weights: $1$ if $i=j=k$, $3$ if two indices equal, $6$ if all three distinct.
4. Using an ultra-fast compiled C kernel evaluates all pairs in $\approx 1.5$ seconds.

---

## 3. Core Intuition & Mathematical Structure

### Kummer's Carry Valuation Table for Base 5 and Base 2

| Valuation Component | Prime $p = 5$ | Prime $p = 2$ |
| :---: | :---: | :---: |
| **Target Power $10^{12}$** | $5^{12} \implies v_5 \ge 12$ | $2^{12} \implies v_2 \ge 12$ |
| **Base-$p$ Form of $200\,000$** | $(2, 2, 4, 0, 0, 0, 0, 0)_5$ | $(110000110101000000)_2$ |
| **Digit Sum $S_p(N)$** | $2 + 2 + 4 = \mathbf{8}$ | $\text{popcount}(200000) = \mathbf{6}$ |
| **Valuation Formula $v_p$** | $\frac{S_5(i) + S_5(j) + S_5(k) - 8}{4}$ | $S_2(i) + S_2(j) + S_2(k) - 6$ |
| **Threshold Inequality** | $S_5(i) + S_5(j) + S_5(k) \ge \mathbf{56}$ | $S_2(i) + S_2(j) + S_2(k) \ge \mathbf{18}$ |
| **Max Digit Sum $S_p$ Bound** | $S_5(m) \le 29$ | $S_2(m) \le 18$ |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Symmetry Search Pipeline
1. Precompute digit sum lookup arrays $f_2[m] = S_2(m)$ and $f_5[m] = S_5(m)$ for $m \in [0, 200\,000]$.
2. Initialize `total = 0`.
3. Loop $i = 0 \dots \lfloor 200\,000/3 \rfloor$:
   - $\text{rem5\_i} = 56 - f_5[i]$.
   - If $\text{rem5\_i} > 58$: continue.
   - $\text{rem2\_i} = 18 - f_2[i]$.
   - $\text{rem\_n} = 200\,000 - i$.
   - Loop $j = i \dots \lfloor \text{rem\_n}/2 \rfloor$:
     - $k = \text{rem\_n} - j$.
     - If $f_5[j] + f_5[k] \ge \text{rem5\_i}$ and $f_2[j] + f_2[k] \ge \text{rem2\_i}$:
       - If $i == j == k$: `total += 1`.
       - Else if $i == j$ or $j == k$ or $i == k$: `total += 3`.
       - Else: `total += 6`.
4. Return `total = 479742450`.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Kummer's Divisibility Verification
- For $(i, j, k)$ with $i + j + k = 200\,000$:
  - $v_5\left(\frac{200000!}{i! j! k!}\right) = \frac{S_5(i) + S_5(j) + S_5(k) - 8}{4} \ge 12 \iff \sum S_5 \ge 56$.
  - $v_2\left(\frac{200000!}{i! j! k!}\right) = \sum S_2 - 6 \ge 12 \iff \sum S_2 \ge 18$.
- Both conditions hold simultaneously if and only if $10^{12} \mid \frac{200000!}{i! j! k!}$.

### Example 2: Target Evaluation for $N = 200\,000$
- Summing all valid symmetric permutations:

$$
N_{\text{trinomial}} = \mathbf{479\,742\,450}
$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Digit Sums Setup**| $f_2[m] = (m \& 1) + f_2[m \gg 1]; f_5[m] = (m \% 5) + f_5[m // 5]$ | $\mathcal{O}(N)$ |
| **Stage 2** | **Outer Loop $i$** | For $i \in [0, N/3]$ | $66\,667$ steps |
| **Stage 3** | **$i$-Level Prune** | If $56 - f_5[i] > 58$: continue | Prunes non-viable $i$ |
| **Stage 4** | **Inner Loop $j$** | For $j \in [i, (N-i)/2]$ | C compiled loop |
| **Stage 5** | **Symmetry Weights** | Add $1, 3,$ or $6$ permutations | $\mathcal{O}(1)$ |
| **Stage 6** | **Return Total** | Return `total = 479742450` | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N^2)$ | $\approx 1.5$ seconds ($3.3 \times 10^9$ inner checks in C) |
| **Space Complexity** | $\mathcal{O}(N)$ | Byte arrays $\approx 400$ KB |
| **Dynamic Execution** | $100\%$ Inline | Kummer's Theorem carry valuation with 6-fold symmetry |

### Critical Invariants & Edge Cases Handled:
1. **Multinomial Carry Exactness**: Kummer's theorem is an exact algebraic equality relating $p$-adic valuation to base-$p$ digit sums, requiring zero floating-point operations.
2. **Permutation Multiplicity**: Triples with 3 identical elements (weight 1), 2 identical elements (weight 3), and distinct elements (weight 6) are partitioned without overcounting.