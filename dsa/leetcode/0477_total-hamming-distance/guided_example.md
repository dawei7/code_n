# Guided Example: Total Hamming Distance

We trace the step-by-step bit-column independence decomposition ($O(N^2) \to O(32N)$), binary vertical slicing across 32 bit positions, count of ones vs zeros ($a \times (n - a)$), and Cartesian pair accumulation on representative numeric arrays:

- **Input:** $nums = [4, 14, 2]$
- **Required output:** `6`
  - Array length: $n = 3$
  - Binary representations (aligned to 4 significant bits):
    $$
    \begin{aligned}
    4  &= 0100_2 \\
    14 &= 1110_2 \\
    2  &= 0010_2
    \end{aligned}
    $$
  - Pairwise Hamming distances:
    - $\text{dist}(4, 14) = \text{dist}(0100_2, 1110_2) = 2$ (differ at bits 1 and 3)
    - $\text{dist}(4, 2) = \text{dist}(0100_2, 0010_2) = 2$ (differ at bits 1 and 2)
    - $\text{dist}(14, 2) = \text{dist}(1110_2, 0010_2) = 2$ (differ at bits 2 and 3)
    - Sum of all pairs: $2 + 2 + 2 = \mathbf{6}$
- **Bit-by-Bit Column Combinatorial Trace:**
  - Let $a_i$ be the count of numbers with bit $i = 1$, and $b_i = n - a_i$ be the count with bit $i = 0$.
  - Every pair formed by one number having `1` and one number having `0` at position $i$ contributes $+1$ to the total distance.
  - **Bit 0 ($2^0$ column):** Bits are $\{0, 0, 0\} \implies a_0 = 0, \; b_0 = 3 \implies 0 \times 3 = \mathbf{0}$
  - **Bit 1 ($2^1$ column):** Bits are $\{0, 1, 1\} \implies a_1 = 2, \; b_1 = 1 \implies 2 \times 1 = \mathbf{2}$
  - **Bit 2 ($2^2$ column):** Bits are $\{1, 1, 0\} \implies a_2 = 2, \; b_2 = 1 \implies 2 \times 1 = \mathbf{2}$
  - **Bit 3 ($2^3$ column):** Bits are $\{0, 1, 0\} \implies a_3 = 1, \; b_3 = 2 \implies 1 \times 2 = \mathbf{2}$
  - Bits 4 through 31: All zeroes $\implies 0 \times 3 = 0$
  - Total Accumulated Hamming Distance:
    $$
    ans = 0 + 2 + 2 + 2 = \mathbf{6}
    $$
- **Duplicate Elements Instance:** $nums = [4, 14, 4] \implies$ pair $(4, 4)$ contributes $0$, while pairs $(4, 14)$ contribute $2 \times 2 = \mathbf{4}$
- **All Identical Elements:** $nums = [7, 7, 7] \implies$ all bits match $\implies \mathbf{0}$

This instance demonstrates vertical bit-slicing and orthogonal combinatorial decomposition, mathematically proves why evaluating bits independently reduces pairwise comparison complexity from $O(N^2)$ to $O(N)$, and derives $O(32N)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $nums = [4, 14, 2]$:
The Hamming distance between two integers is the number of positions at which their corresponding binary bits differ.
Return the **sum of Hamming distances** between all pairs of integers in $nums$.

```text
Pairwise Approach (O(N^2)):
  dist(4, 14) = 2
  dist(4,  2) = 2
  dist(14, 2) = 2
  Total: 2 + 2 + 2 = 6

Column-by-Column Combinatorial Approach (O(N)):
  Number  Bit 3  Bit 2  Bit 1  Bit 0
    4:      0      1      0      0
   14:      1      1      1      0
    2:      0      0      1      0
  ---------------------------------
  Ones (a): 1      2      2      0
  Zeroes(b):2      1      1      3
  Pairs (a*b): 2   2      2      0

Total Hamming Distance = 2 + 2 + 2 + 0 = 6
```

### The Inefficiency of Pairwise Scanning
A brute-force loop tests all $\binom{N}{2} = \frac{N(N-1)}{2}$ pairs.
For $N = 10^4$, $\binom{N}{2} \approx 5 \times 10^7$ pairs, with 32-bit comparisons per pair, resulting in $1.6 \times 10^9$ operations (Time Limit Exceeded).
To solve this in linear time:
We invert the loop order: instead of summing over all pairs and inspecting 32 bits, **we sum over the 32 bit positions and count how many pairs differ at each bit!**

---

## 2. Conceptual Foundation & Invariants

### 1. Bit Independence:
The total Hamming distance is the sum of differences across all bit positions:
$$
\text{Total Distance} = \sum_{u < v} \sum_{i=0}^{31} (nums[u] \oplus nums[v])_i = \sum_{i=0}^{31} \sum_{u < v} (nums[u] \oplus nums[v])_i
$$

### 2. Cartesian Product Counting at Bit $i$:
At bit position $i$, each number in $nums$ has either a `1` or a `0`:
- Let $a_i = \sum_{x \in nums} (x \gg i) \ \& \ 1$ be the number of elements with a `1` at bit $i$.
- Let $b_i = n - a_i$ be the number of elements with a `0` at bit $i$.
- A pair $(u, v)$ differs at bit $i$ if and only if one element has a `1` and the other has a `0`.
- The number of such differing pairs is the product:
  $$
  \text{Pairs differing at bit } i = a_i \times b_i = a_i \times (n - a_i)
  $$
- Summing over all 32 bit columns:
  $$
  \text{Total Hamming Distance} = \sum_{i=0}^{31} a_i (n - a_i)
  $$

> **Column Sum Invariant.** The contribution of bit position $i$ to the total Hamming distance across all pairs depends solely on the number of set bits $a_i$ at that column, independent of the values of any other bits.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [4, 14, 2]$ ($n = 3$):
Initialize $ans = 0$.

---

### Step 1: Column 0 ($i = 0$, Value $2^0$)
- Bits of $[4, 14, 2]$:
  - $4 \gg 0 \ \& \ 1 = 0$
  - $14 \gg 0 \ \& \ 1 = 0$
  - $2 \gg 0 \ \& \ 1 = 0$
- Count of ones: $a_0 = 0$.
- Count of zeroes: $b_0 = 3 - 0 = 3$.
- Contribution:
  $$
  a_0 \times b_0 = 0 \times 3 = \mathbf{0}
  $$
- $ans \leftarrow 0 + 0 = 0$.

---

### Step 2: Column 1 ($i = 1$, Value $2^1$)
- Bits of $[4, 14, 2]$:
  - $4 \gg 1 \ \& \ 1 = 0$
  - $14 \gg 1 \ \& \ 1 = 1$
  - $2 \gg 1 \ \& \ 1 = 1$
- Count of ones: $a_1 = 2$ (from numbers $14$ and $2$).
- Count of zeroes: $b_1 = 3 - 2 = 1$ (from number $4$).
- Contribution:
  $$
  a_1 \times b_1 = 2 \times 1 = \mathbf{2}
  $$
  (Pairs: $(4, 14)$ and $(4, 2)$ differ at bit 1).
- $ans \leftarrow 0 + 2 = 2$.

---

### Step 3: Column 2 ($i = 2$, Value $2^2$)
- Bits of $[4, 14, 2]$:
  - $4 \gg 2 \ \& \ 1 = 1$
  - $14 \gg 2 \ \& \ 1 = 1$
  - $2 \gg 2 \ \& \ 1 = 0$
- Count of ones: $a_2 = 2$ (from numbers $4$ and $14$).
- Count of zeroes: $b_2 = 3 - 2 = 1$ (from number $2$).
- Contribution:
  $$
  a_2 \times b_2 = 2 \times 1 = \mathbf{2}
  $$
  (Pairs: $(4, 2)$ and $(14, 2)$ differ at bit 2).
- $ans \leftarrow 2 + 2 = 4$.

---

### Step 4: Column 3 ($i = 3$, Value $2^3$)
- Bits of $[4, 14, 2]$:
  - $4 \gg 3 \ \& \ 1 = 0$
  - $14 \gg 3 \ \& \ 1 = 1$
  - $2 \gg 3 \ \& \ 1 = 0$
- Count of ones: $a_3 = 1$ (from number $14$).
- Count of zeroes: $b_3 = 3 - 1 = 2$ (from numbers $4$ and $2$).
- Contribution:
  $$
  a_3 \times b_3 = 1 \times 2 = \mathbf{2}
  $$
  (Pairs: $(14, 4)$ and $(14, 2)$ differ at bit 3).
- $ans \leftarrow 4 + 2 = 6$.

---

### Step 5: Columns 4 to 31
- All elements $< 16$, so bits $4 \dots 31$ are zero for all numbers:
  $$
  a_i = 0 \implies a_i \times (3 - 0) = 0
  $$

---

### Final Total:
$$
ans = 0 + 2 + 2 + 2 = \mathbf{6}
$$

---

## 4. Complete Execution Trace

| Bit Index $i$ | Binary Weight $2^i$ | Numbers with Bit $= 1$ | Ones Count $a_i$ | Zeroes Count $b_i$ | Pairs Differing ($a_i \times b_i$) | Cumulative Distance |
|:---:|:---:|:---|:---:|:---:|:---:|:---:|
| **$0$** | $1$ | None | $0$ | $3$ | $0 \times 3 = 0$ | $0$ |
| **$1$** | $2$ | $14, 2$ | $2$ | $1$ | $2 \times 1 = \mathbf{2}$ | $2$ |
| **$2$** | $4$ | $4, 14$ | $2$ | $1$ | $2 \times 1 = \mathbf{2}$ | $4$ |
| **$3$** | $8$ | $14$ | $1$ | $2$ | $1 \times 2 = \mathbf{2}$ | **$6$** |
| **$4 \dots 31$** | $\ge 16$ | None | $0$ | $3$ | $0 \times 3 = 0$ | **$6$** |
| **Final** | — | — | — | — | — | **Result: $6$** |

---

## 5. Boundary Cases & Failure Modes

- **Single Element ($N = 1$):** No pairs exist $\implies a_i \times (1 - a_i) = 0 \times 1 = \mathbf{0}$.
- **All Identical Numbers ($[5, 5, 5, 5]$):** For every bit, either $a_i = 4, b_i = 0$ or $a_i = 0, b_i = 4 \implies a_i \times b_i = 0 \implies \mathbf{0}$.
- **Complementary Pairs ($[0, 2^{31} - 1]$):** At all 31 bits, $a_i = 1, b_i = 1 \implies 31 \times 1 = \mathbf{31}$.
- **Large $N = 10^4$:** $32 \times 10^4 = 3.2 \times 10^5$ operations (executes in $< 10$ ms).

---

## 6. Traps & Common Anti-Patterns

- **Generating All Pairs:** Running nested loops `for i in range(n): for j in range(i+1, n)` causes TLE. The column-wise counting algorithm runs in linear time.
- **Integer Overflow in Pair Multiplication:** For $N = 10^5$, $a \approx 50,000$ and $b \approx 50,000 \implies a \times b \approx 2.5 \times 10^9$. Over 32 bits, the sum can reach $8 \times 10^{10}$, exceeding signed 32-bit integers. Accumulators must be 64-bit integers (`long long`).
- **Assuming Bit Length Bounded by Smallest Element:** Scanning only up to $\max(nums)$'s bit length is a valid optimization, but fixed 32-bit scanning guarantees completeness with zero branching overhead.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - The outer loop iterates over the 32 bit positions.
  - The inner loop iterates over all $N$ numbers to count set bits.
  - Total Time: $\mathcal{O}(32 \cdot N) = \mathcal{O}(N)$. For $N = 10^4$, $3.2 \times 10^5$ operations, running in $< 8$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ space using scalar accumulators.
